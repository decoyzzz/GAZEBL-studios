import os
import random
import arcade
import time

import ASCII
import sounds
from lib import s, get_key
from classesSpell import IceSpell

clear = lambda: os.system('cls')

class Charik:

    def __init__(self,name = "unnamed Charik", hp = 10):
        self.name = name
        self.hp = hp
        self.alive = True
        self.freezebuildup = 0
        self.fire_dot_damage = 0

    def getDamage(self, damage):
        self.hp -= damage
        self.hp = max(0, self.hp)
        if self.hp <= 0:
            self.alive = False

    def attack(self, target):
        self.damage = random.randint(1, 3)
        target.getDamage(self.damage)

        clear()
        print(ASCII.drawbossattack)
        arcade.play_sound(sounds.bossattack)
        print (f"{self.name} {s('dealt')} {target.name} {self.damage} {s('damage!')}!")

    def makeMove(self, enemy):
        if self.alive == False:
            clear()
            print(ASCII.drawbossdead)
            print(f"{self.name} {s('is_dead!')}")
        
        else:

            if self.freezebuildup > 0:
                
                clear()
                print(ASCII.drawbossfreeze)
                print(f"{self.name} {s('is_freezed_and_skips_their_move!')}")
                
                self.freezebuildup -= 1

            else:
                self.attack(enemy)

            if self.fire_dot_damage > 0:
                time.sleep(1.9)
                clear()
                print(ASCII.drawbossfiredamage)
                arcade.play_sound(sounds.burningsound)
                print(f"{self.name} {s('takes')} {self.fire_dot_damage} {s('fire_damage!')}")

                self.getDamage(self.fire_dot_damage)
                self.fire_dot_damage -= 1


class Player(Charik):

    def __init__(self, name="Player", hp=10, mana=0):
        super().__init__(name, hp)
        self.mana = mana
        self.spells=[]
        self.weapons=[]

    def castSpell(self, spell, target):
        spell.cast(self, target)

    def attackWithWeapon(self, weapon, target):
        weapon.attack(self, target)

    def makeMove(self, enemy):

        if self.alive == False:

            clear()
            print(ASCII.drawplayerdead.format(playername=self.name))
            print(s('YOU_LOOSE!'))

            # os.system("shutdown /s /t 5")
            # return
            exit()
        
        elif self.freezebuildup > 0:

            clear()
            print(ASCII.drawtemplate)
            arcade.play_sound(sounds.iceshardsound)
            print(f"{self.name} {s('is_freezed_for')} {self.freezebuildup} {s('more_moves!')}")
            
            self.freezebuildup -= 1

        else:
            #Переменные для хода игрока
            self.heal = random.randint(1, 3)
            
            #Цикл игрока
            while True:
                clear()
                print(ASCII.drawmain.format(playername=self.name, bossname=enemy.name))
                print(f"{s('your_hp')}: {self.hp} | {s('your_mana')}: {self.mana} | {s('enemys_hp')}: {enemy.hp}\n [1] Выбрать оружие для атаки! [2] Восстановить здоровье! [3] Выбрать заклинание для атаки!")
                action = get_key()

                match action:
                    #Меню оружия
                    case 1:
                        print("\nДоступное оружие:")
                        for i in range(len(self.weapons)):
                            weapon = self.weapons[i]
                            if weapon.minDamage != weapon.maxDamage:
                                print(f"[{i+1}] {weapon.name}! ({s('Damage')}: {weapon.minDamage}-{weapon.maxDamage})")
                            else : 
                                print(f"[{i+1}] {weapon.name}! ({s('Damage')}: {weapon.minDamage})")

                        print(f"[{len(self.weapons) + 1}] {s('back')}!")
                        
                        choice = get_key()
                        if choice in range(1, len(self.weapons)+1):
                            self.attackWithWeapon(self.weapons[choice-1], enemy)
                            return
                        
                        #крит для меча
                        # if random.random() > 0.66:
                        #     self.mana += self.damage
                        #     self.damage = self.damage * 2
                        #     enemy.getDamage(self.damage)

                        #     clear()
                        #     print(ASCII.drawswordcrit)
                        #     arcade.play_sound(sounds.swordsound)
                        #     print(f"{self.name} нанёс {self.damage} критического урона! Здоровье {enemy.name}: {enemy.hp}")
                        #     return


                        # else:
                        #     self.mana += self.damage
                        #     enemy.getDamage(self.damage)

                        #     clear()
                        #     print(ASCII.drawsword)
                        #     arcade.play_sound(sounds.swordsound)
                        #     print(f"{self.name} нанёс {self.damage} урона! Здоровье {enemy.name}: {enemy.hp}")
                        #     return

                    #Хилка
                    case 2:
                        if self.hp >= 20:
                            self.getDamage(self.heal)

                            clear()
                            print(ASCII.drawtemplate)
                            print(f"Еблан? У тебя фулл хп. Лося за втык! Хилка нанесла {self.heal} урона! Текущее здоровье {self.hp}")
                            return

                        else:
                            self.hp = min(self.heal + self.hp, 20)

                            clear()
                            print(ASCII.drawheal)
                            arcade.play_sound(sounds.healsound)
                            print(f"Хилка дала {self.heal} ХП. Текущее здоровье :{self.hp} ")
                            return


                    #Меню выбора навыков
                    case 3:
                        print("\nДоступные заклинания:")
                        for i in range(len(self.spells)):
                            spell = self.spells[i]
                            print(f"[{i+1}] {spell.name}! ({s('cost')}: {spell.manaCost})")

                        print(f"[{len(self.spells) + 1}] {s('back')}!")
                        
                        choice = get_key()
                        if choice in range(1, len(self.spells)+1):
                            self.castSpell(self.spells[choice-1], enemy)
                            return
                        elif choice == 7:
                            self.castSpell(IceSpell("Снежная лавина", 50, 50, 0, 1, 10), enemy)
                            return
                        
                        # print(f"\nДоступные навыки:\n[1] Фаерболл! [2] Ледяной осколок! [3] Вернуться назад!")
                        # skillchoise = lib.get_key()

                        # match skillchoise:
                        #     #Выбор фаербола
                        #     case 1:
                        #         fireball = Fireball("Фаерболл", 2, 4, 3, 0.5, 3)
                        #         self.castSpell(fireball, enemy)
                        #         return


                        #     #Ледяной урон
                        #     case 2:
                        #         iceshard = IceShard("Морозная свежесть", 1, 2, 3, 0.5, 2)
                        #         self.castSpell(iceshard, enemy)
                        #         return


                        #     #Вернуться назад
                        #     case 3:
                        #        continue

class Enemy(Charik):
    def __init__(self, name = "unnamed Enemy", hp = 10, minDamage = 1, maxDamage = 3):
        self.name = name
        self.hp = hp
        self.minDamage = minDamage
        self.maxDamage = maxDamage
        self.alive = True
        self.freezebuildup = 0
        self.fire_dot_damage = 0

    def attack(self, target):
        self.damage = random.randint(self.minDamage, self.maxDamage)
        target.getDamage(self.damage)

        clear()
        print(ASCII.drawbossattack)
        arcade.play_sound(sounds.bossattack)
        print (f"{self.name} {s('dealt')} {target.name} {self.damage} {s('damage!')}!")