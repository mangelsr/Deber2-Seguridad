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
    number = ''
    for character in message:
        if ord(character) in range(48, 58):
            number += character
        else:
            if (number != ''):
                decoded += chr(int(number) + 64)
            if (character != '-'):
                decoded += character
            number = ''
    if number != '':
        decoded += chr(int(number) + 64)
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

mensaje = "18-23-20-19-20 8-15-21-4-3-6-19-5 22-12-19-23-21-16-19-20 22-25 5-3-10"
print(combined(mensaje))

mensaje = "4-16-19 4-23-12-19'5 4-9-12-20, 4-16-19 5-3-11-11-19-6'5 20-9-10-19"
print(combined(mensaje))

mensaje = "15-10 11-19-11-9-6-15-19-5 4-16-19 8-15-10-19-5 5-4-15-12-12 8-12-23-25"
print(combined(mensaje))