import json
import os
from datetime import date, time, datetime

history_lst = []


def load():
    base = os.getcwd()
    path = os.path.join(base, "commands.json")
    with open(path, "r") as f:
        a = json.load(f)
    return a


def dump(a):
    base = os.getcwd()
    path = os.path.join(base, "commands.json")
    with open(path, "w") as f:
        json.dump(a, f, indent=2)
    return a


def recors_his(func):
    def wrapper(*args, **kwargs):
        history_lst.append(func.__name__)
        return func(*args, **kwargs)

    return wrapper


@recors_his
def help(text=None):
    data = load()
    print("commands:", *data["commands"], sep=" | ")


def exit(text=None):
    print("Goodbye!")
    return False


@recors_his
def clear(text=None):
    return os.system("cls" if os.name == "nt" else "clear")


@recors_his
def add(text):
    a = load()
    a["add"].append(text)
    dump(a)


@recors_his
def list(text=None):
    a = load()
    for i, d in enumerate(a["add"], start=1):
        print(f"{i}. {d}")


@recors_his
def delete(index):
    a = load()
    try:
        if 0 < int(index) <= len(a["add"]):
            a["add"].pop(int(index) - 1)
        else:
            print("index out of range")
    except ValueError:
        print("ValueError")
    dump(a)


@recors_his
def date_(text=None):
    print(date.today())


@recors_his
def time_(text=None):
    t = datetime.now().time()
    print(t.strftime("%H:%M:%S"))


@recors_his
def history(text=None):
    for i in history_lst:
        print(i)


@recors_his
def find(text):
    a = load()
    for i, d in enumerate(a["add"], start=1):
        if text.lower() in d.lower():
            print(f"{i}. {d}")


@recors_his
def edit(text):
    a = load()
    text = text.split(" ", 1)
    try:
        if 0 < int(text[0]) <= len(a["add"]):
            if len(text) > 1:
                a["add"][int(text[0]) - 1] = text[1]
                dump(a)
            else:
                print("invalid sintax")
        else:
            print("index out of range")
    except ValueError:
        print("invalid index")


@recors_his
def count(text=None):
    a = load()
    print("elements in the notes:", len(a["add"]))


@recors_his
def del_all(text=None):
    a = load()
    confid = input("Are you sure? (y/n): ")
    if confid == "y":
        a["add"] = []
        dump(a)
    elif confid == "n":
        print("operation canceled")
    else:
        print("invalid value")


def backup(text=None):
    i = 1
    a = load()
    base = os.getcwd()
    while os.path.exists(os.path.join(base, f"commands{i}.json")):
        i += 1
    filename = f"commands{i}.json"
    path = os.path.join(base, filename)
    with open(path, "w") as f:
        json.dump(a, f, indent=2)
    print(f"Backup saved as {filename}")


data = {
    "help": help,
    "exit": exit,
    "clear": clear,
    "add": add,
    "list": list,
    "del": delete,
    "date": date_,
    "time": time_,
    "history": history,
    "find": find,
    "edit": edit,
    "count": count,
    "del_all": del_all,
    "backup": backup,
}
