from commands import data

circle = True


while circle:
    cmd = input(">>> ")
    cmd = cmd.split(" ", 1)
    if cmd[0] in data:
        if cmd[0] == "exit":
            circle = data[cmd[0]](cmd)
            continue
        data[cmd[0]](cmd[1 if len(cmd) > 1 else 0])
    else:
        print("Not command")
