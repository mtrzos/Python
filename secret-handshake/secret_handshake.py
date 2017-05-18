def addSignalToCommands( count, commands ):
    if count == 0:
        commands.append("wink")
    elif count == 1:
        commands.append("double blink")
    elif count == 2:
        commands.append("close your eyes")
    elif count == 3:
        commands.append("jump")
    elif count == 4:
        commands.reverse()


def handshake(code):
    count = 0
    commands = []
    print code
    code = int(str(code[::-1]))
    while code > 0:
        if (code % 2) == 0:
            addSignalToCommands( count, commands )
        code = code / 2
        count ++ 1
    return commands







def code():
    pass
