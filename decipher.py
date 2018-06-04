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
    dictionary = {
        'Z':'A', 'Y':'B', 'X':'C', 'W':'D' , 'V':'E', 'U':'F', 'T':'G', 'S':'H', 'R':'I', 'Q':'J',
        'P':'K', 'O':'L', 'N':'M', 'M':'N' , 'L':'O', 'K':'P', 'J':'Q', 'I':'R', 'H':'S', 'G':'T',
        'F':'U', 'E':'V', 'D':'W', 'C':'X' , 'B':'Y', 'A':'Z'
    }
    decoded = ""
    for character in message:
        if character in dictionary:
            decoded += dictionary[character]
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