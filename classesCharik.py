import os
import random
import arcade
import time

import ASCII
import sounds
import lib
from classesSpell import Fireball, IceShard

clear = lambda: os.system('cls')

class Charik:

    def __init__(self,name = "unnamed", hp = 10, mana = 0):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.alive = True
        self.freezebuildup = 0
        self.fire_dot_damage = 0

    def getDamage(self, damage):
        self.hp -= damage
        self.hp = max(0, self.hp)
        if self.hp <= 0:
            self.alive = False

    def attack(self, target, damage=1):
        target.getDamage(damage)

        clear()
        print(ASCII.drawbossattack)
        arcade.play_sound(sounds.bossattack)
        print (f"{self.name} нанёс {target.name} {self.damage} урона!")

    def makeMove(self, enemy):
        if self.alive == False:
            clear()
            print(ASCII.drawbossdead)
            print(f"{self.name} мертв!")
        
        else:

            if self.freezebuildup > 0:
                
                clear()
                print(ASCII.drawbossfreeze)
                print(f"{self.name} заморожен и пропускает ход!")
                
                self.freezebuildup -= 1

            else:
                self.damage = random.randint(1, 3)
                self.attack(enemy, self.damage)

            if self.fire_dot_damage > 0:
                time.sleep(1.4)
                clear()
                print(ASCII.drawbossfiredamage)
                arcade.play_sound(sounds.burningsound)
                print(f"{self.name} получает {self.fire_dot_damage} урон от огня")

                self.getDamage(self.fire_dot_damage)
                self.fire_dot_damage -= 1


class Player(Charik):

    def __init__(self, name="Player", hp=-1, mana=-1):
        super().__init__(name, hp, mana)
        self.spells=[]

    def castSpell(self, spell, target):
        spell.cast(self, target)

    def makeMove(self, enemy):

        if self.alive == False:

            clear()
            print(ASCII.drawtemplate)
            print(f"ТЫ ПРОИГРАЛ!")

            os.system("shutdown /s /t 5")
            return
        
        elif self.freezebuildup > 0:

            clear()
            print(ASCII.drawtemplate)
            arcade.play_sound(sounds.iceshardsound)
            print(f"{self.name} заморожен еще {self.freezebuildup} ход(а)!")
            
            self.freezebuildup -= 1

        else:
            #Переменные для хода игрока
            self.damage = random.randint(1, 3)
            self.heal = random.randint(1, 3)
            
            #Цикл игрока
            while True:
                clear()
                print(ASCII.drawmain.format(playername=self.name))
                print(f"Твоё хп: {self.hp} | Твоя мана: {self.mana} | Хп Босса: {enemy.hp}\n [1] Ударить мечом! [2] Восстановить здоровье! [3] Меню выбора навыков!")
                action = lib.get_key()

                match action:
                    #Удар мечом
                    case 1:
                        #крит для меча
                        if random.random() > 0.66:
                            self.mana += self.damage
                            self.damage = self.damage * 2
                            enemy.getDamage(self.damage)

                            clear()
                            print(ASCII.drawswordcrit)
                            arcade.play_sound(sounds.swordsound)
                            print(f"{self.name} нанёс {self.damage} критического урона! Здоровье {enemy.name}: {enemy.hp}")
                            return


                        else:
                            self.mana += self.damage
                            enemy.getDamage(self.damage)

                            clear()
                            print(ASCII.drawsword)
                            arcade.play_sound(sounds.swordsound)
                            print(f"{self.name} нанёс {self.damage} урона! Здоровье {enemy.name}: {enemy.hp}")
                            return

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
                        print(f"\nДоступные навыки:\n[1] Фаерболл! [2] Ледяной осколок! [3] Вернуться назад!")
                        skillchoise = lib.get_key()

                        match skillchoise:
                            #Выбор фаербола
                            case 1:
                                fireball = Fireball("Фаерболл", 2, 4, 3, 0.5, 3)
                                self.castSpell(fireball, enemy)
                                return


                            #Ледяной урон
                            case 2:
                                iceshard = IceShard("Ледяной осколок", 1, 2, 3, 0.5, 2)
                                self.castSpell(iceshard, enemy)
                                return


                            #Вернуться назад
                            case 3:
                               continue