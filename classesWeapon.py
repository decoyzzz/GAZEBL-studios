import os
import random
import arcade

import ASCII

clear = lambda: os.system('cls')

class Weapon:
    def __init__(self, name, minDamage, maxDamage, manaPerHit, critChance, critMultiplier, drawning, drawningCrit, sound):
        self.name = name
        self.minDamage = minDamage
        self.maxDamage = maxDamage
        self.manaPerHit = manaPerHit
        self.critChance = critChance
        self.critMultiplier = critMultiplier
        self.drawning = drawning
        self.drawningCrit = drawningCrit
        self.sound = sound

    def attack(self, attacker, target):
        self.damage = random.randint(self.minDamage, self.maxDamage)

        #крит для оружия
        if random.random() < self.critChance:
            attacker.mana += self.damage
            self.damage = self.damage * 2
            target.getDamage(self.damage)

            clear()
            if self.drawningCrit != None: print(self.drawningCrit)
            else: print(ASCII.drawtemplate)
            if self.sound != None: arcade.play_sound(self.sound)
            print(f"{attacker.name} атакует с {self.name} и наносит {self.damage} критического урона! Здоровье {target.name}: {target.hp}")
            return

        else:
            attacker.mana += self.damage
            target.getDamage(self.damage)

            clear()
            if self.drawning != None: print(self.drawning)
            else: print(ASCII.drawtemplate)
            if self.sound != None: arcade.play_sound(self.sound)
            print(f"{attacker.name} атакует с {self.name} и наносит {self.damage} урона! Здоровье {target.name}: {target.hp}")
            return