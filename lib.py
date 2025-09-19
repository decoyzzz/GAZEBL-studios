import msvcrt
import importlib

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

#Функция для считывания стрингов с разных языковых папок    
def s(lang, stringName):
    strings = importlib.import_module(f"lang.{lang}.strings")
    return strings.strings.get(stringName, stringName)