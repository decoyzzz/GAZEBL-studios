import os
import arcade
import sounds

import ASCII

clear = lambda: os.system('cls')

class Potion:
    def __init__(self, name, count, strength):
        self.name = name
        self.count = count
        self.strength = strength

class HealPotion(Potion):
    def affect(self, recipient):
        if self.count > 0:
            recipient.getHealed(self.strength)
            self.count -= 1

            clear()
            print(ASCII.drawheal)
            arcade.play_sound(sounds.healsound)
            print(f"{self.name} дало {self.strength} ХП. Текущее здоровье :{recipient.hp} ")
            return

class ManaPotion(Potion):
    def affect(self, recipient):
        if self.count > 0:
            recipient.restoreMana(self.strength)
            self.count -= 1

        clear()
        print(ASCII.drawtemplate)
        arcade.play_sound(sounds.healsound)
        print(f"{self.name} дало {self.strength} маны. Текущая мана :{recipient.mana} ")
        return