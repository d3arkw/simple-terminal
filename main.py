import json
import os
from commands import data

circle = True


while circle:
    cmd = input(">>> ")
    cmd = cmd.split(" ", 1)
    if cmd[0] in data:
        if cmd == "exit":
            circle = data[cmd]()
            continue
        if cmd[0] == 'add':
            data[cmd[0]](cmd[1])
            continue
        data[cmd[0]](cmd)
    else:
        print("Not command")
