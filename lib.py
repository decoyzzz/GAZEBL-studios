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


_strings = None
l = None
def chooseLanguage():
    global l, _strings
    while l not in ("en","ru"):
        clear()
        print("Choose language / Выберите язык ")
        print("[1] English(WIP) [2] Русский")
        choice = get_key()

        match choice:
            case 1: l = "en"
            case 2: l = "ru"

    if getattr(sys, 'frozen', False):
        # exe
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(__file__)

    # Добавляем путь к lang в sys.path, чтобы importlib его нашёл
    sys.path.append(os.path.join(base_path, "lang"))

    _strings = importlib.import_module(f"{l}.strings").strings

def s(stringName):
    global _strings
    return _strings.get(stringName, stringName)