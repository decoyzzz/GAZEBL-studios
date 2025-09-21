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
            print(f"{recipient.name} выпил {self.name}. Текущее здоровье: {recipient.hp}")
            return

class ManaPotion(Potion):
    def affect(self, recipient):
        if self.count > 0:
            recipient.restoreMana(self.strength)
            self.count -= 1

        clear()
        print(ASCII.drawtemplate)
        arcade.play_sound(sounds.healsound)
        print(f"{recipient.name} выпил {self.name}. Текущая мана: {recipient.mana}")
        return