class Cipher(object):
    globalKey = ''
    def __init__(self, key):
        keyStr = ''
        for char in key:
            keyStr += str(ord(char) % 97)
            print("Printing key: %s" % str(ord(char) % 97))
        self.globalKey = int(keyStr)
        print(self.globalKey)

    def encode(self, plainText):
        return plainText


class Caesar(object):
    globalKey = 3
    def __init__(self):
        pass

    def encode(self, plainText):
        cipherText = ""
        for character in plainText.lower():
            if ord(character) + self.globalKey > 122 and character.isalpha():
                cipherText += chr(96 + ((ord(character) + self.globalKey) % 122))
            elif character.isalpha():
                cipherText += chr(ord(character) + self.globalKey)

        return cipherText

    def decode(self, cipherText):
        plainText = ""
        for character in cipherText.lower():
            if ord(character) - self.globalKey < 97 and character.isalpha():
                plainText += chr(122 - ((ord(character) - self.globalKey) % 97))
            elif character.isalpha():
                plainText += chr(ord(character) - self.globalKey)

        return plainText
