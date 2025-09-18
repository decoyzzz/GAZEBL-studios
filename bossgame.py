import os
import time
import msvcrt

import ASCII
import bossGrisha

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

#Переменные игрока
playerhp = int(20)
playermana = int(0)

#Пасхалкоу
if playername == "Аллах":
    playerhp = int(999)
    playermana = int(999)

bossGrisha.bossGrishaCycle()

#Смерть босса
clear()
print(ASCII.drawbossdead)
print(f"Ты убил босса!")
time.sleep(1.35)
exit()