#cmd to create exe file
#python -m PyInstaller --onefile bossgame.py --add-data "sounds;sounds" --add-data "lang;lang"

import os
import time
import arcade

import sounds
import ASCII
from lib import chooseLanguage, get_key, s

from classesCharik import Player, Enemy
from classesSpell import FireSpell, IceSpell, HealSpell
from classesWeapon import Weapon
from classesPotion import HealPotion, ManaPotion

clear = lambda: os.system('cls')

#LOX 4

#Language selection
chooseLanguage()

#Playername's input and validating
clear()
playername = input(s("enter_your_name"))
while len(playername) > 5 or len(playername) < 3:
    clear()
    print("Размер имени от 3 до 5 символов...")
    playername = input(s("enter_your_name"))

#Usernames for tests
match playername:
    case "Аллах" | "Allah":
        player = Player(playername, 9999, 9999, 9999)
    case "dodik":
        player = Player(playername, 1, 0)
    case _:
        player = Player(playername, 100, 0)

# Giving the player a weapon: Weapon(name, minDamage, maxDamage, +manaPerHit, critChance, critMultiplier, image, critImage, sound)
stick = Weapon(s("wooden_stick"), 5, 5, 5, 0.2, 5, None, None, sounds.sticksound)
player.weapons.append(stick)

# Giving the player a potion
player.potions.append(HealPotion("Зелье здоровья", 2, 20))
player.potions.append(ManaPotion("Зелье магии", 2, 25))

player.spells.append(HealSpell("Лечение", 20, 25))
    
# Creating the first enemy
worm = Enemy("Червь", 25, 5, 5)

while worm.alive == True:
    player.makeMove(worm)
    time.sleep(1.9)

    worm.makeMove(player)
    time.sleep(1.9)


#First victory screen
clear()
print(ASCII.drawtrophy)
arcade.play_sound(sounds.victorysound)
print(f"{s('you_defeated')} {worm.name}!")
time.sleep(3)

#Giving the player a sword 
clear()
print(ASCII.drawtemplate)
sword = Weapon(s("sword"), 8, 12, 10, 0.5, 2, ASCII.drawsword, ASCII.drawswordcrit, sounds.swordsound)
player.weapons.append(sword)
print(f"Новое оружие получено: {sword.name}!")
time.sleep(1.9)

# Creating the second enemy
fatWorm = Enemy("Жирный червь", 75, 5, 10)

while fatWorm.alive == True:
    player.makeMove(fatWorm)
    time.sleep(1.9)

    fatWorm.makeMove(player)
    time.sleep(1.9)

# Second victory screen
clear()
print(ASCII.drawtrophy)
arcade.play_sound(sounds.victorysound)
print(f"{s('you_defeated')} {fatWorm.name}!")
time.sleep(3)

# Giving the player 1 spell to choose
while len(player.spells) == 1:
    clear()
    print(ASCII.drawtemplate)
    print("Тебе доступно 1 заклинание на выбор:")
    print("[1]Фаерболл! [2]Ледяной осколок")
    choice = get_key()
    match choice:
        case 1: player.spells.append(FireSpell(s("fireball"), 10, 20, 15, 0.5, 15))
        case 2: player.spells.append(IceSpell(s("iceshard"), 5, 10, 15, 0.5, 2))
        case _: pass

#Third enemy creating
wormKing = Enemy("Король червей", 150, 10, 15)

while wormKing.alive == True:
    player.makeMove(wormKing)
    time.sleep(1.9)

    wormKing.makeMove(player)
    time.sleep(1.9)

#Third victory screen
clear()
print(ASCII.drawtrophy)
arcade.play_sound(sounds.victorysound)
print(f"{s('you_defeated')} {wormKing.name}!")
time.sleep(3)


# Giving the player spells: Spell(name, minDamage, maxDamage, manaCost)
# For FireSpell, the last two values are burn chance and duration; for IceSpell, freeze chance and duration
# player.spells.append(FireSpell(s("fireball"), 2, 4, 3, 0.5, 3))
# player.spells.append(IceSpell(s("iceshard"), 1, 2, 3, 0.5, 2))
# player.spells.append(FireSpell(s("ignition"), 0, 1, 2, 1, 2))

print("Press any key to exit...")
get_key()