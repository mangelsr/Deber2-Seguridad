
def decodeVigenere(cipherText, key):
    decoded = ""
    #to equals the lenghts
    if( len(cipherText) > len(key) ):
        n = ( len(cipherText)//len(key) ) + 1
        key = key * n
    #to move the itr in the key
    pos = 0
    #char by char
    for character in cipherText:

        cipherCharNum = ord(character)

        #decoding: reverse the operation of the coding
        decodedCharNum = cipherCharNum - ( ord( key [pos] ) - 65 )

        #fix the position
        if( decodedCharNum < 65 ):
            decodedCharNum = 90 - ( 65 - decodedCharNum ) + 1

        decoded += chr( decodedCharNum )
        pos += 1

    return decoded


def caesar(message, steps):
    decoded = ""
    for character in message:
        if ord(character) in range(65, 91):
            if (ord(character) - steps) < 65:
                decoded += chr(ord(character) - steps + 26)
            else:
                decoded += chr(ord(character) - steps)
        else:
            decoded += character
    return decoded


#decode caesar cipher of 3 letters forward
def caesar_3forward(message):

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


#decode caesar cipher of 2 letters forward
def caesar_2forward(message):
    decoded = ""
    for character in message:
        #get ASCII decimal representation of only Uppercase Alphabet
        if ord(character) in range(65, 91):
            #check if is A or B
            if ord(character)>=65 and ord(character)<=66:
                #add offset of 26 letters and substract 2 positions
                decoded += chr(ord(character) + 26 - 2)
            else:     
                decoded += chr(ord(character) - 2)
        else:
            decoded += character
    return decoded


#decode caesar cipher of three letters back
def caesar_3back(message):
    decoded = ""
    for character in message:
        #get ASCII decimal representation of only Uppercase Alphabet
        if ord(character) in range(65, 91):
            #check if is X,Y or Z
            if ord(character)>=88 and ord(character)<=90:
                #substract offset of 26 letters and add 3 positions
                decoded += chr(ord(character) - 26 +3)
            else:     
                decoded += chr(ord(character) + 3)
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
    return caesar_3forward(atbash(a1z26(message)))


#decode binary message, 8bits characters
def binary(message):
  result=""
  s=message #temp variable for input string
  n=len(s)//8 # number of letters in message  
  b="00001000"# binary string of 8 bits  
  for i in range(0,n):
    b=s[0:8] #get first 8 bits    
    result+=chr( int(b,2) ) # take b to int and then get ASCII value   
    s=s[8:] #get rid of first 8 bits 
  return result


def show_info(info):
    alogithm = info['type']
    if alogithm == 'Caesar':
        if 'steps' in info.keys():
            message = caesar(info['cypher_text'], 2)
        else:
            message = caesar(info['cypher_text'], 3)
    elif alogithm == 'Atbash':
        message = atbash(info['cypher_text'])
    elif alogithm == 'A1Z26':
        message = a1z26(info['cypher_text'])
    elif alogithm == 'Combined':
        message = combined(info['cypher_text'])
    print('Cypher Text: {} -> Message: {}'.format(info['cypher_text'], message))


episodes = {
    1: {'cypher_text': 'ZHOFRPH WR JUDYLWB IDOOV.', 'type': 'Caesar'},
    2: {'cypher_text': 'QHAW ZHHN: UHWXUQ WR EXWW LVODQG.', 'type': 'Caesar'},
    3: {'cypher_text': "KH'V VWLOO LQ WKH YHQWV.", 'type': 'Caesar'},
    4: {'cypher_text': "FDUOD, ZKB ZRQ'W BRX FDOO PH?", 'type': 'Caesar'},
    5: {'cypher_text': "RQZDUGV DRVKLPD!", 'type': 'Caesar'},
    6: {'cypher_text': 'PU. FDHVDULDQ ZLOO EH RXW QHAW ZHHN. PU. DWEDVK ZLOO VXEVWLWXWH.', 'type': 'Caesar'},
    7: {'cypher_text': 'KZKVI QZN WRKKVI HZBH: "ZFFTSDCJSTZWHZWFS!"', 'type': 'Atbash'},
    8: {'cypher_text': 'V. KOFIRYFH GIVNYOVB.', 'type': 'Atbash'},
    9: {'cypher_text': 'MLG S.T. DVOOH ZKKILEVW.', 'type': 'Atbash'},
    10: {'cypher_text': 'HLIIB, WRKKVI, YFG BLFI DVMWB RH RM ZMLGSVI XZHGOV.', 'type': 'Atbash'},
    11: {'cypher_text': 'GSV RMERHRYOV DRAZIW RH DZGXSRMT.', 'type': 'Atbash'},
    12: {'cypher_text': 'YILFTSG GL BLF YB SLNVDLIP: GSV XZMWB.', 'type': 'Atbash'},
    13: {'cypher_text': 'SVZEB RH GSV SVZW GSZG DVZIH GSV UVA.', 'type': 'Atbash'},
    14: {'cypher_text': '14-5-24-20 21-16: \"6-15-15-20-2-15-20 20-23-15: 7-18-21-14-11-12-5\'19 7-18-5-22-5-14-7-5.\"', 'type': 'A1Z26'},
    15: {'cypher_text': '22-9-22-1-14 12-15-19 16-1-20-15-19 4-5 12-1 16-9-19-3-9-14-1.', 'type': 'A1Z26'},
    16: [
            {'cypher_text': 'SXEHUWB LV WKH JUHDWHVW PBVWHUB RI DOO DOVR: JR RXWVLGH DQG PDNH IULHQGV.', 'type': 'Caesar'},
            {'cypher_text': '2-21-20 23-8-15 19-20-15-12-5 20-8-5 3-1-16-5-18-19?', 'type': 'A1Z26'},
    ],
    17: {'cypher_text': '8-1-16-16-25 14-15-23, 1-18-9-5-12?', 'type': 'A1Z26'},
    18: [
            {'cypher_text': 'OLHV', 'type': 'Caesar'},
            {'cypher_text': '9-20 23-15-18-11-19 6-15-18 16-9-9-9-9-9-9-9-9-9-9-9-9-9-9-9-9-9-7-19!', 'type': 'A1Z26'},
    ],
    19: [
            {'cypher_text': 'PBVWHUB VKDFN', 'type': 'Caesar'},
            {'cypher_text': 'SLWW', 'type': 'Caesar'},
            {'cypher_text': 'OAUVG', 'type': 'Caesar', 'steps': 2},
            {'cypher_text': 'EWTUG AQW OCTKNAP', 'type': 'Caesar', 'steps': 2},
            {'cypher_text': '20-15 2-5 3-15-14-20-9-14-21-5-4...', 'type': 'A1Z26'},
    ],
    20: [
            {'cypher_text': 'ELOO LV ZDWFKLQJ', 'type': 'Caesar'},
            {'cypher_text': '18-5-22-5-18-19-5 20-8-5 3-9-16-8-5-18-19', 'type': 'A1Z26'},
            {'cypher_text': '5-19-23-6-21-16 18-9-6 4-16-19 22-12-15-10-20-19-25-19', 'type': 'Combined'},
    ],
}


for k,v in episodes.items():
    print('-------------- {} --------------'.format(k))
    if isinstance(v, dict):
        show_info(v)
    else:
        for i in v:
            show_info(i)
    print()