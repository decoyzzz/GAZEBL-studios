import os, sys
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
    global l
    lang = l

    if getattr(sys, 'frozen', False):
        # путь для exe
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(__file__)

    # формируем полный путь к модулю
    sys.path.append(os.path.join(base_path, "lang"))

    strings = importlib.import_module(f"{lang}.strings")
    return strings.strings.get(stringName, stringName)