import os
import time
import arcade

import sounds
import ASCII
from lib import chooseLanguage, get_key, s

from classesCharik import Player, Enemy
from classesSpell import FireSpell, IceSpell
from classesWeapon import Weapon

clear = lambda: os.system('cls')

#LOX 4

#Выбор языка
chooseLanguage()

#Считывание и проверка длины имени игрока
playername = input(s("enter_your_name"))
while len(playername) > 5 or len(playername) < 3:
    print("Размер имени от 3 до 5 символов...")
    playername = input(s("enter_your_name"))

#Пасхалкоу
match playername:
    case "Аллах" | "Allah":
        player = Player(playername, 999, 999)
    case "dodik":
        player = Player(playername, 1, 0)
    case _:
        player = Player(playername, 20, 0)

#Выдача оружия игроку: Weapon(название, минУрон, максУрон, +манаЗаУдар, вероятностьКрита, мультиплаерКрита, рисунок, рисунокКрита, звук)
stick = Weapon(s("wooden_stick"), 1, 1, 1, 0.2, 5, None, None, sounds.sticksound)
player.weapons.append(stick)

    
#Создание первого врага
worm = Enemy("Червь", 5, 1, 1)

while worm.alive == True:
    player.makeMove(worm)
    time.sleep(1.9)

    worm.makeMove(player)
    time.sleep(1.9)


#Экран победы над первым врагом
clear()
print(ASCII.drawtrophy)
arcade.play_sound(sounds.victorysound)
print(f"{s('you_defeated')} {worm.name}!")
time.sleep(5)

#Выдача игроку меча
clear()
print(ASCII.drawtemplate)
sword = Weapon(s("sword"), 1, 3, 2, 0.5, 2, ASCII.drawsword, ASCII.drawswordcrit, sounds.swordsound)
player.weapons.append(sword)
print(f"Новое оружие получено: {sword.name}!")
time.sleep(1.9)

#Создание второго врага
fatWorm = Enemy("Жирный червь", 15, 1, 2)

while fatWorm.alive == True:
    player.makeMove(fatWorm)
    time.sleep(1.9)

    fatWorm.makeMove(player)
    time.sleep(1.9)

#Экран победы над вторым врагом
clear()
print(ASCII.drawtrophy)
arcade.play_sound(sounds.victorysound)
print(f"{s('you_defeated')} {fatWorm.name}!")
time.sleep(5)

#Выдача заклинания на выбор
while len(player.spells) == 0:
    clear()
    print(ASCII.drawtemplate)
    print("Тебе доступно 1 заклинание на выбор:")
    print("[1]Фаерболл! [2]Ледяной осколок")
    choice = get_key()
    match choice:
        case 1: player.spells.append(FireSpell(s("fireball"), 2, 4, 3, 0.5, 3))
        case 2: player.spells.append(IceSpell(s("iceshard"), 1, 2, 3, 0.5, 2))
        case _: pass

#Создание третьего врага
wormKing = Enemy("Король червей", 30, 2, 3)

while wormKing.alive == True:
    player.makeMove(wormKing)
    time.sleep(1.9)

    wormKing.makeMove(player)
    time.sleep(1.9)

#Экран победы над третьим врагом
clear()
print(ASCII.drawtrophy)
arcade.play_sound(sounds.victorysound)
print(f"{s('you_defeated')} {wormKing.name}!")
time.sleep(5)


#Выдача заклинаний игроку: Spell(название, минУрон, максУрон, ценаМана)
# У FireSpell два последние значения это вероятность поджога и длительность, у IceSpell - вероятность фризза и длительность
# player.spells.append(FireSpell(s("fireball"), 2, 4, 3, 0.5, 3))
# player.spells.append(IceSpell(s("iceshard"), 1, 2, 3, 0.5, 2))
# player.spells.append(FireSpell(s("ignition"), 0, 1, 2, 1, 2))