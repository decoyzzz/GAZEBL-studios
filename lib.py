import os
import msvcrt
import importlib

clear = lambda: os.system('cls')

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

l = None
def chooseLanguage():
    global l
    while l != "en" and l !="ru":
        clear()
        print("Choose language / Выберите язык ")
        print("[1]English [2]Русский")
        choice = get_key()

        match choice:
            case 1: l = "en"
            case 2: l = "ru"
            case _: pass

#Функция для считывания стрингов с разных языковых папок    
def s(lang, stringName):
    lang = l
    strings = importlib.import_module(f"lang.{lang}.strings")
    return strings.strings.get(stringName, stringName)