import math

def decimalToBinary(number):
    array = []
    var = int(number)
    while var > 0:
        remainder = var % 2
        array.append(remainder)
        var = math.floor(var / 2)

    for digit in array:
        if digit == 0:
            print("I am zero")
        else:
            print("I am one!")

    return str(array)