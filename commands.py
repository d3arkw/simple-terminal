import json
import os
from datetime import date, time, datetime

history_lst = []


def recors_his(func):
    def wrapper(*args, **kwargs):
        history_lst.append(func.__name__)
        return func(*args, **kwargs)

    return wrapper


@recors_his
def help(text=None):
    base = os.path.dirname(__file__)
    path = os.path.join(base, "commands.json")
    data = {}
    with open(path, "r") as f:
        data = json.load(f)
    print(*data["commands"], sep=" | ")
    data


def exit(text=None):
    print("Goodbye!")
    return False


@recors_his
def clear(text=None):
    return os.system("cls" if os.name == "nt" else "clear")


@recors_his
def add(text):
    base = os.path.dirname(__file__)
    path = os.path.join(base, "commands.json")
    a = ""
    with open(path, "r") as f:
        a = json.load(f)
    a["add"].append(text)
    with open(path, "w") as f:
        json.dump(a, f, indent=2)


@recors_his
def list(text=None):
    base = os.path.dirname(__file__)
    path = os.path.join(base, "commands.json")
    a = ""
    with open(path, "r") as f:
        a = json.load(f)
    for i, d in enumerate(a["add"], start=1):
        print(f"{i}. {d}")


@recors_his
def delete(index):
    base = os.path.dirname(__file__)
    path = os.path.join(base, "commands.json")
    a = ""
    with open(path, "r") as f:
        a = json.load(f)
    try:
        a["add"].pop(int(index) - 1)
    except ValueError:
        print("ValueError")
    with open(path, "w") as f:
        json.dump(a, f, indent=2)


@recors_his
def datenow(text=None):
    print(date.today())


@recors_his
def timenow(text=None):
    t = datetime.now().time()
    print(t.strftime("%H:%M:%S"))


@recors_his
def history(text=None):
    for i in history:
        print(i)


data = {
    "help": help,
    "exit": exit,
    "clear": clear,
    "add": add,
    "list": list,
    "del": delete,
    "date": datenow,
    "time": timenow,
    "history": history,
}
history = []
