import os
import time
import arcade

import sounds
import ASCII
from lib import chooseLanguage, s, l

from classesCharik import Charik, Player
from classesSpell import FireSpell, IceSpell
from classesWeapon import Weapon

clear = lambda: os.system('cls')

#LOX 4

#Выбор языка
chooseLanguage()

#Считывание и проверка длины имени игрока
playername = input(s(l,"enter_your_name"))
while len(playername) > 5 or len(playername) < 3:
    print("Размер имени от 3 до 5 символов...")
    playername = input(s(l,"enter_your_name"))

#Пасхалкоу
if playername in ("Аллах", "Allah"):
    player = Player(playername, 999, 999)
else:
    player = Player(playername, 20, 0)

#Выдача оружия игроку: Weapon(название, минУрон, максУрон, +манаЗаУдар, вероятностьКрита, мультиплаерКрита, рисунок, рисунокКрита, звук)
sword = Weapon(s(l,"sword"), 1, 3, 2, 0.5, 2, ASCII.drawsword, ASCII.drawswordcrit, sounds.swordsound)
stick = Weapon(s(l,"wooden_stick"), 1, 1, 1, 0.1, 10, None, None, sounds.sticksound)

player.weapons.append(sword)
player.weapons.append(stick)

#Выдача заклинаний игроку: Spell(название, минУрон, максУрон, ценаМана)
# У FireSpell два последние значения это вероятность поджога и длительность, у IceSpell - вероятность фризза и длительность
player.spells.append(FireSpell(s(l,"fireball"), 2, 4, 3, 0.5, 3))
player.spells.append(IceSpell(s(l,"iceshard"), 1, 2, 3, 0.5, 2))
player.spells.append(FireSpell(s(l,"ignition"), 0, 1, 2, 1, 2))
    
#Создание первого босса
firstBoss = Charik(s(l,"lolik"), 35)

while firstBoss.alive == True:
    player.makeMove(firstBoss)
    time.sleep(1.9)

    firstBoss.makeMove(player)
    time.sleep(1.9)


#Экран победы над первым боссом
clear()
print(ASCII.drawtrophy)
arcade.play_sound(sounds.victorysound)
print(f"{s(l,'you_defeated')} {firstBoss.name}!")
time.sleep(5)
exit()