import math

validCodes = ['wink', 'double blink', 'close your eyes', 'jump']

def handshake(code):
    count = 0
    commands = []
    code = code
    if type(code) is str:
        for char in code[::-1]:
            if char  == '1':
                addSignalToCommands( count, commands )
            if char  != '1' and char != '0':
                return []
            count += 1
    else:
        while code > 0:
            if (code % 2) == 1:
                addSignalToCommands( count, commands )
            code = math.floor(code / 2)
            count += 1
    return commands


def code(arr):
    code = 0
    lastIndex = 0
    for count, item in enumerate(arr):
        if item in validCodes:
            code += addDigitToCode(item, code)
            if validCodes.index(item) < lastIndex and code < 9999:
                code += 10000
            lastIndex = validCodes.index(item)
        else:
            return '0'
    return str(code)

def addSignalToCommands( count, commands ):
    if count == 0:
        commands.append('wink')
    elif count == 1:
        commands.append('double blink')
    elif count == 2:
        commands.append('close your eyes')
    elif count == 3:
        commands.append('jump')
    elif count == 4:
        commands.reverse()

def addDigitToCode( count, code ):
    if count == 'wink':
        return 1
    elif count == 'double blink':
        return 10
    elif count == 'close your eyes':
        return 100
    elif count == 'jump':
        return 1000
    else:
        return 0









