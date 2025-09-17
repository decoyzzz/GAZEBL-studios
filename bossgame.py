import random
import os
import time
import arcade

clear = lambda: os.system('cls')

#LOX 2

#Считывание и проверка длины имени игрока
playername = input("Введи своё имя: ")
while len(playername) > 5 or len(playername) < 3:
    print("Размер имени от 3 до 5 символов...")
    playername = input("Введи своё имя: ")

def refteshscreen_time():
    time.sleep(1.35)
    clear()



drawmain = fr"""
======================================
|      {playername}           Гриша   
|                 *   ,   ,        * |
|  *     0           (\_o_/)  *      |
|*      /|\   *      (  ^  )     *   |
|_______/_\__________/|   |\_________|
|                    _(   )_         |
======================================
"""


drawsword = fr"""
======================================
|   ↑             /\    ↑            |
|        ↑        ||             ↑   |
|                 ||                 |
|                 ||   ↑             |
|    ↑       ↑  ======             ↑ |
|                 ||        ↑        |
======================================        
"""

drawheal = fr"""
======================================
|               _  _              ♥  |
|  ♥          /` \/ `\     ♥         |
|        ♥    \      /               |
|              '.  .'                |
|     ♥          \/             ♥    |
|                      ♥             |
======================================
"""

drawbossattack = fr"""
======================================
|           <      ,    ,    <       |
| <               (\_o_/)            |
|    <=====       (  ^  )        <   |
|                 /|   |\            |
|              <                     |
|       <                     <      |
======================================    
"""

drawbossdead = fr"""
======================================
|           *      ,    ,   *        |
|      X          (\_o_/)       X    |
|                 ( X X )            |
|          X      (  x  )            |
|    *            /|   |\     *      |
|                                    |
======================================    
"""

drawfireballsucces = """
======================================
|               >                    |
|   >   0/                    >      |
|      /|     ============>          |
|      / \                           |
|   >                  >             |
|         >                       >  |
======================================
"""

drawfireballfailed = """
======================================
|       X        \|/            X    |
|  X           0/-o--    X           |
|             /| /|\                 |
|       X     / \             X      |
|                    X               |
|     X                           X  |
======================================
"""

drawtemplate = """
======================================
|                                    |
|                                    |
|                                    |
|                                    |
|                                    |
|                                    |
======================================
"""




playerhp = int(20)
playermana = int(0)
bosshp = int(20)
fire_dot_damage = -1
freezebuildup = -1

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
    icesharddamage = random.randint(1, 3)

    #Проверка на смерть босса
    if bosshp < 1:
        refteshscreen_time()
        print(drawbossdead)
        print(f"Ты убил босса!")
        exit()

    refteshscreen_time()
    print(drawmain)

    #логика игрока

    action = int(input(f"Твоё хп: {playerhp} | Твоя мана: {playermana} | Хп Босса: {bosshp}\n [1] чтобы нанести урон! [2] Восстановить здоровье! [3] Меню выбора навыков!"))
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


    #меню выбора навыков
    elif action == 3:
        skillchoise = int(input(f"\nДоступные навыки:\n[1] Фаерболл! [2] ICEnoName! [3] Вернуться назад!"))


        #выбор фаербола
        if skillchoise == 1:
            refteshscreen_time()

            print(drawfireballsucces)

            bosshp -= fireballdamage
            playermana -= 3

            print (f"Нанесенно: {fireballdamage} Здоровье босса: {bosshp}")

            #шанс прока дот урона от огня
            if random.random() < 0.5:
                refteshscreen_time()
                fire_dot_damage = 3
                print(f"Босс загорелся на 3 хода!")
        #если не хватает маны
        elif skillchoise == 1 and playermana <3:
            refteshscreen_time()
            playerhp -= 1
            print(drawfireballfailed)
            print (f"Фаерболл взорвался в руке и нанёс 1 урона! Текущее здоровье: {playerhp}")


        #ледяной урон
        elif skillchoise == 2:
            refteshscreen_time()
            playermana -= 3
            bosshp -= icesharddamage
            print(f"IceNoName нанёс {icesharddamage} Здоровье босса: {bosshp}")

            if random.random() < 0.5:
                freezebuildup = 2
        elif skillchoise == 3:
            continue

    #логика босса
    if freezebuildup > 0:
        refteshscreen_time()
        print(f"Босс заморожен на {freezebuildup} хода!")
        freezebuildup -= 1
    else:
        refteshscreen_time()

        print(drawbossattack)

        arcade.play_sound(bossattack)

        bdamage = random.randint(1, 3)
        playerhp -= bdamage
        print (f"Босс Гриша нанёс {bdamage} урона!")


    #Счётчик дот урона от фаерболла
    if fire_dot_damage >= 0:
        fire_dot_damage -= 1
        bosshp -= fire_dot_damage


    if playerhp <= 0:
        os.system("shutdown /s /t 5")
        break