import random
import os
import time
import arcade
import sys
import msvcrt

clear = lambda: os.system('cls')

#LOX 2

playername = input("Введи своё имя: ")

def refteshscreen_time():
    time.sleep(1)
    clear()



drawmain = fr"""
======================================
|       {playername}       Монстр    
|        O            ,   ,          |
|       /|\          (\_o_/)         |
|       / \          (  ^  )         |
|                    /|   |\         |
|                                    |
======================================
"""


drawsword = r"""
======================================
|                 /\                 |
|                 ||                 |
|                 ||                 |
|                 ||                 |
|               ======               |
|                 ||                 |
======================================        
"""

drawheal = r"""
======================================
|               _  _                 |
|             /` \/ `\               |
|             \      /               |
|              '.  .'                |
|                \/                  |
|                                    |
======================================
"""

drawbossattack = fr"""
======================================
|                  ,    ,            |
|                 (\_o_/)            |
|    <=====       (  ^  )            |
|                 /|   |\            |
|                                    |
|                                    |
======================================    
"""




playerhp = int(20)
playermana = int(0)
bosshp = int(20)

swordsound = arcade.load_sound("sounds/sword.wav")
healsound = arcade.load_sound("sounds/heal.wav")
bossattack = arcade.load_sound("sounds/bossattack.wav")


#if playername == "Аллах":
    #playerhp = int(999)

while True:
    #Переменные урона и хила вынес в начало цикла
    pdamage = random.randint(1, 3)
    playerheal = random.randint(1, 3)
    fireballdamage = random.randint(2, 6)




    refteshscreen_time()
    print(drawmain)

    #логика игрока

    action = int(input(f"Твоё хп: {playerhp}  Твоя мана: {playermana} Хп Босса: {bosshp}\n /1/ чтобы нанести урон! /2/ Восстановить здоровье! /3/ Фаерболл!"))
    if action == 1:

        refteshscreen_time()

        print(drawsword)

        arcade.play_sound(swordsound)

        playermana += pdamage
        bosshp -= pdamage
        print(f"{playername} нанёс {pdamage} урона! Здоровье Гриши: {bosshp}")


    elif action == 2:


        if playerhp >= 20:
            playerhp -= playerheal
            print(f"Еблан? У тебя фулл хп. Лося за втык! Хилка нанесла {playerheal} урона! Текущее здоровье {playerhp}")




        else:
             refteshscreen_time()

             arcade.play_sound(healsound)

             playerhp = min(playerheal + playerhp, 20)

             print(drawheal)

             print(f"Хилка дала {playerheal} Текущее здоровье {playerhp} ")

    elif action == 3 and playermana > 2.9:
        bosshp -= fireballdamage
        playermana -= 3
        print (f"Нанесенно: {fireballdamage} Здоровье босса: {bosshp}")

    elif action == 3 and playermana < 3:
        playerhp -= 1
        print (f"Фаерболл взорвался в руке и нанёс 1 урона! Текущее здоровье: {playerhp}")







    #логика босса

    refteshscreen_time()

    print(drawbossattack)

    arcade.play_sound(bossattack)

    bdamage = random.randint(1, 3)
    playerhp -= bdamage
    print (f"Босс Гриша нанёс {bdamage} урона!")




    if playerhp <= 0:
        os.system("shutdown /s /t 5")
        break