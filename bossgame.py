import random
import os
import time
import arcade
import ASCII

clear = lambda: os.system('cls')

#LOX 3

#Считывание и проверка длины имени игрока
playername = input("Введи своё имя: ")
while len(playername) > 5 or len(playername) < 3:
    print("Размер имени от 3 до 5 символов...")
    playername = input("Введи своё имя: ")

#Функция очистки
def refreshscreen_time():
    time.sleep(1.35)
    clear()


#Переменные
playerhp = int(20)
playermana = int(0)
bosshp = int(20)

fire_dot_damage = -1
freezebuildup = -1

#Звуки
swordsound = arcade.load_sound("sounds/sword.wav")
healsound = arcade.load_sound("sounds/heal.wav")
bossattack = arcade.load_sound("sounds/bossattack.wav")
fireballsound = arcade.load_sound("sounds/fireball.wav")
iceshardsound = arcade.load_sound("sounds/iceshard.wav")

#Пасхалкоу
if playername == "Аллах":
    playerhp = int(999)
    playermana = int(999)

#Основной цикл
while True:
    #Переменные урона, хилла и скиллов
    pdamage = random.randint(1, 3)
    playerheal = random.randint(1, 3)
    fireballdamage = random.randint(2, 4)
    icesharddamage = random.randint(1, 2)

    #Переменные для босса
    bdamage = random.randint(1, 3)

    #Проверка на смерть босса
    if bosshp < 1:
        refreshscreen_time()
        print(ASCII.drawbossdead)
        print(f"Ты убил босса!")
        exit()

    #Главный экран
    refreshscreen_time()
    print(ASCII.drawmain.format(playername=playername))


    #Логика игрока
    action = int(input(f"Твоё хп: {playerhp} | Твоя мана: {playermana} | Хп Босса: {bosshp}\n [1] Ударить мечом! [2] Восстановить здоровье! [3] Меню выбора навыков!"))

    match action:

        #Удар мечом
        case 1:

            #крит для меча
            if random.random() > 0.01:
                refreshscreen_time()
                arcade.play_sound(swordsound)
                print(ASCII.drawsword)

                playermana = pdamage
                pdamage = pdamage * 1.5
                bosshp -= pdamage

                print(f"{playername} нанёс {pdamage} критического урона! Здоровье Гриши: {bosshp}")

            else:
                refreshscreen_time()
                arcade.play_sound(swordsound)
                print(ASCII.drawsword)

                playermana += pdamage
                bosshp -= pdamage

                print(f"{playername} нанёс {pdamage} урона! Здоровье Гриши: {bosshp}")

        #Хилка
        case 2:
            if playerhp >= 20:
                playerhp -= playerheal
                print(f"Еблан? У тебя фулл хп. Лося за втык! Хилка нанесла {playerheal} урона! Текущее здоровье {playerhp}")

            else:
                refreshscreen_time()
                arcade.play_sound(healsound)

                playerhp = min(playerheal + playerhp, 20)

                print(ASCII.drawheal)
                print(f"Хилка дала {playerheal} Текущее здоровье {playerhp} ")


        #Меню выбора навыков
        case 3:
            skillchoise = int(input(f"\nДоступные навыки:\n[1] Фаерболл! [2] Ледяной осколок! [3] Вернуться назад!"))

            match skillchoise:
                #Выбор фаербола
                case 1:
                    if playermana >= 3:

                        refreshscreen_time()
                        arcade.play_sound(fireballsound)
                        print(ASCII.drawfireballsucces)

                        bosshp -= fireballdamage
                        playermana -= 3

                        print (f"Нанесенно: {fireballdamage} Здоровье босса: {bosshp}")

                    #шанс прока дот урона от огня
                        if random.random() < 0.5:

                            refreshscreen_time()
                            fire_dot_damage = 3

                            print(ASCII.drawtemplate)
                            print(f"Босс загорелся на 3 хода!")
                #Если не хватает маны
                    else:
                        refreshscreen_time()

                        playerhp -= 1

                        print(ASCII.drawfireballfailed)
                        print (f"Фаерболл взорвался в руке и нанёс 1 урона! Текущее здоровье: {playerhp}")


                #Ледяной урон
                case 2:
                    if playermana >= 3:
                        refreshscreen_time()
                        arcade.play_sound(iceshardsound)

                        playermana -= 3
                        bosshp -= icesharddamage

                        print(ASCII.drawtemplate)
                        print(f"Ледяной осколок нанёс {icesharddamage} Здоровье босса: {bosshp}")

                        if random.random() < 0.5:
                            freezebuildup = 2

                    #Если не хватает маны
                    else:
                        playerhp -= 1

                        print(ASCII.drawtemplate)
                        print(f"Ледяной осколок обморозил руку и нанёс 1 урона! Текущее здоровье: {playerhp} ")

                #Вернуться назад
                case 3:
                    continue



    #Проверка Босса на Фриз
    if freezebuildup > 0:
        refreshscreen_time()
        arcade.play_sound(iceshardsound)

        freezebuildup -= 1

        print(ASCII.drawbossfreeze)
        print(f"Босс заморожен на {freezebuildup} хода!")


    #Логика босса
    else:
        refreshscreen_time()
        print(ASCII.drawbossattack)
        arcade.play_sound(bossattack)

        bdamage = random.randint(1, 3)
        playerhp -= bdamage

        print (f"Босс Гриша нанёс {bdamage} урона!")


    #Счётчик дот урона от фаерболла
    if fire_dot_damage >= 0:
        refreshscreen_time()

        fire_dot_damage -= 1
        bosshp -= fire_dot_damage

        print(ASCII.drawtemplate)
        arcade.play_sound(fireballsound)
        print("Босс получает 1 урон от огня")


    if playerhp <= 0:
        os.system("shutdown /s /t 5")
        break