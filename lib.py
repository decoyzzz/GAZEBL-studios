import os, sys
import msvcrt
import importlib

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# Function to read the pressed key
def get_key():
    #clearing the buffer
    while msvcrt.kbhit():
        msvcrt.getch()

    key = msvcrt.getch()  # reading only the latest key press
    try:
        return int(key.decode())
    except ValueError:
        return None  # if not a number


_strings = None
l = None
def chooseLanguage():
    global l, _strings
    while l not in ("en","ru","pl"):
        clear()
        print("Choose language / Wybierz język / Выберите язык ")
        print("[1] English [2] Polski [3] Русский")
        choice = get_key()

        match choice:
            case 1: l = "en"
            case 2: l = "pl"
            case 3: l = "ru"

    if getattr(sys, 'frozen', False):
        # exe
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(__file__)

    #Adding the path to lang in sys.path so that importlib can find it
    sys.path.append(os.path.join(base_path, "lang"))

    _strings = importlib.import_module(f"{l}.strings").strings

def s(stringName):
    global _strings
    return _strings.get(stringName, stringName)