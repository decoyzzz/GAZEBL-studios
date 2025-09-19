import os
import time

import sounds
import ASCII

from classesCharik import Charik, Player
from classesSpell import Fireball, IceShard
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

#Выдача оружия игроку
player.weapons.append(Weapon("Меч", 1, 3, 2, 0.5, 2, ASCII.drawsword, ASCII.drawswordcrit, sounds.swordsound))
player.weapons.append(Weapon("Деревянная палка", 1, 1, 1, 0.5, 2, None, None, None))

#Выдача заклинаний игроку
player.spells.append(Fireball("Фаерболл", 2, 4, 3, 0.5, 3))
player.spells.append(IceShard("Ледяная стрела", 1, 2, 3, 0.5, 2))
    
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
print(f"Ты победил босса {bossLelik.name}!")
time.sleep(1.35)
exit()