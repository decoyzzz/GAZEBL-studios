import os
import time
import arcade

import sounds
import ASCII

from classesCharik import Charik, Player
from classesSpell import FireSpell, IceSpell
from classesWeapon import Weapon

clear = lambda: os.system('cls')

#LOX 4

#Считывание и проверка длины имени игрока
playername = input("Введи своё имя: ")
while len(playername) > 5 or len(playername) < 3:
    print("Размер имени от 3 до 5 символов...")
    playername = input("Введи своё имя: ")

#Пасхалкоу
if playername in ("Аллах", "Allah"):
    player = Player(playername, 999, 999)
else:
    player = Player(playername, 20, 0)

#Выдача оружия игроку: Weapon(название, минУрон, максУрон, +манаЗаУдар, вероятностьКрита, мультиплаерКрита, рисунок, рисунокКрита, звук)
player.weapons.append(Weapon("Меч", 1, 3, 2, 0.5, 2, ASCII.drawsword, ASCII.drawswordcrit, sounds.swordsound))
player.weapons.append(Weapon("Деревянная палка", 1, 1, 1, 0.1, 10, None, None, sounds.sticksound))

#Выдача заклинаний игроку: Spell(название, минУрон, максУрон, ценаМана)
# У FireSpell два последние значения это вероятность поджога и длительность, у IceSpell - вероятность фризза и длительность
player.spells.append(FireSpell("Фаерболл", 2, 4, 3, 0.5, 3))
player.spells.append(IceSpell("Ледяной осколок", 1, 2, 3, 0.5, 2))
player.spells.append(FireSpell("Поджог", 0, 1, 2, 1, 2))
    
#Создание первого босса
bossLelik = Charik("Лёлик", 35)

while bossLelik.alive == True:
    player.makeMove(bossLelik)
    time.sleep(1.7)

    bossLelik.makeMove(player)
    time.sleep(1.7)


#Экран победы над первым боссом
clear()
print(ASCII.drawtrophy)
arcade.play_sound(sounds.victorysound)
print(f"Ты победил босса {bossLelik.name}!")
time.sleep(5)
exit()