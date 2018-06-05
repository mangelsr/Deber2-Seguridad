def caesar(message):
    decoded = ""
    for character in message:
        if ord(character) in range(65, 91):
            if ord(character)>=65 and ord(character)<=67:
                decoded += chr(ord(character) - 3 + 26)
            else:     
                decoded += chr(ord(character) - 3)
        else:
            decoded += character
    return decoded


def atbash(message):
    decoded = ""
    for character in message:
        if ord(character) in range(65, 91):
            decoded += chr(90 - (ord(character) % 65))
        else:
            decoded += character
    return decoded


def a1z26(message):
    decoded = ""
    message = message.split(' ')
    for word in message:
        letter = word.split('-')
        for character in letter:
            if not character.isdigit():
                special_chars = [',', "'", '"', '.', ':', ';', '!', '?']
                for c in special_chars:
                    character = character.replace(c, '')
                decoded += chr(int(character) + 64)
            else:
                decoded += chr(int(character) + 64)
        decoded += ' '
    return decoded


def combined(message):
    return caesar(atbash(a1z26(message)))

mensaje = "VWDQ LV QRW ZKDW KH VHHPV"
print(caesar(mensaje))

mensaje = "MLG S.T. DVOOH ZKKILEVW"
print(atbash(mensaje))

mensaje = "8-1-16-16-25 14-15-23, 1-18-9-5-12?"
print(a1z26(mensaje))

mensaje = "5-19-23-6-21-16 18-9-6 4-16-19 22-12-15-10-20-19-25-19"
print(combined(mensaje))