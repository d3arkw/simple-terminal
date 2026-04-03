import json
import os


def help(text=None):
    base = os.path.dirname(__file__)
    path = os.path.join(base, "commands.json")
    data = {}
    with open(path, "r") as f:
        data = json.load(f)
    print(*data["commands"], sep=" | ")


def exit(text=None):
    print("Goodbye!")
    return False


def clear(text=None):
    print(os.system("cls" if os.name == "nt" else "clear"))


def add(text):
    base = os.path.dirname(__file__)
    path = os.path.join(base, "commands.json")
    a = ""
    with open(path, "r") as f:
        a = json.load(f)
    a["add"].append(text)
    with open(path, "w") as f:
        json.dump(a, f)


def list(text = None):
    base = os.path.dirname(__file__)
    path = os.path.join(base, "commands.json")
    a = ''
    with open(path,'r') as f:
        a = json.load(f)
    for i in a['add']:
        print(i)


data = {"help": help, "exit": exit, "clear": clear, "add": add, "list": list}
