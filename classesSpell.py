import os
import random
import arcade
import time

import ASCII
import sounds

clear = lambda: os.system('cls')

class Spell:
    def __init__(self, name, minDamage, maxDamage, manaCost):
        self.name = name
        self.minDamage = minDamage
        self.maxDamage = maxDamage
        self.manaCost = manaCost

class FireSpell(Spell):
    def __init__(self, name, minDamage, maxDamage, manaCost, burningChance, burningStrength):
        super().__init__(name, minDamage, maxDamage, manaCost)
        self.burningChance = burningChance
        self.burningStrength = burningStrength

    def cast(self, spellcaster, target):
        if spellcaster.mana >= self.manaCost:
            
            self.damage = random.randint(self.minDamage, self.maxDamage)
            target.getDamage(self.damage)
            spellcaster.mana -= self.manaCost
            
            clear()
            print(ASCII.drawfireballsucces)
            arcade.play_sound(sounds.fireballsound)
            print (f"{self.name} нанес: {self.damage} урона! Здоровье {target.name}: {target.hp}")
            
            #шанс прока дот урона от огня
            if random.random() < self.burningChance:
                target.fire_dot_damage = self.burningStrength

                time.sleep(1.9)
                clear()
                print(ASCII.drawbossfiredamage)
                arcade.play_sound(sounds.burningsound)
                print(f"{target.name} загорелся на {self.burningStrength} хода(ов)!")
        
        #Если не хватает маны
        else:
            spellcaster.getDamage(1)
           
            clear()
            print(ASCII.drawfireballfailed)
            print (f"{self.name} взорвался в руке {spellcaster.name} и нанёс 1 урона! Текущее здоровье: {spellcaster.hp}")

class IceSpell(Spell):
    def __init__(self, name, minDamage, maxDamage, manaCost, freezeChance, freezeStrength):
        super().__init__(name, minDamage, maxDamage, manaCost)
        self.freezeChance = freezeChance
        self.freezeStrength = freezeStrength

    def cast(self, spellcaster, target):
        if spellcaster.mana >= self.manaCost:
            
            self.damage = random.randint(self.minDamage, self.maxDamage)
            spellcaster.mana -= self.manaCost
            target.getDamage(self.damage)

            clear()
            print(ASCII.drawiceshardsucces)
            arcade.play_sound(sounds.iceshardsound)
            print(f"{self.name} нанёс {self.damage} урона! Здоровье {target.name}: {target.hp}")

            if random.random() < self.freezeChance:
                target.freezebuildup = self.freezeStrength

                time.sleep(1.9)
                clear()
                print(ASCII.drawbossfreeze)
                print(f"{self.name} заморозил {target.name} на {self.freezeStrength} хода(ов)!")
                                    
            return
                                

        #Если не хватает маны
        else:
            spellcaster.getDamage(1)

            clear()
            print(ASCII.drawfireballfailed)
            print(f"{self.name} обморозил руку и нанёс 1 урона! Текущее здоровье: {spellcaster.hp} ")
            return
        
class HealSpell(Spell):
    def __init__(self, name, healPoints, manaCost):
        self.name = name
        self.healPonts = healPoints
        self.manaCost = manaCost

    def cast(self, spellcaster, target):
        if spellcaster.useMana(self.manaCost):
            
            spellcaster.getHealed(self.healPonts)

            clear()
            print(ASCII.drawfireballfailed)
            print(f"{spellcaster.name} использует лечащее заклинание! Здоровье {spellcaster.name}: {spellcaster.hp}")                 
            return