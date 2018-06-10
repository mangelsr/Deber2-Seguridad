
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

mensaje="01010000011101010111010000100000011000010110110001101100001000000111001101101001011110000010000001110000011010010110010101100011011001010111001100100000011101000110111101100111011001010111010001101000011001010111001000100001"
print(binary(mensaje))
print()

mensaje = "PU. FDHVDULDQ ZLOO EH RXW QHAW ZHHN. PU. DWEDVK ZLOO VXEVWLWXWH. "
print(caesar_3forward(mensaje))
print()


mensaje = "EWTUG AQW OCTKNAP"
print(caesar_2forward(mensaje))
print()


mensaje = "TEV FP TBKAV PL MBOCBZQ"
print(caesar_3back(mensaje))
print()


mensaje = "MLG S.T. DVOOH ZKKILEVW"
print(atbash(mensaje))
print()


mensaje = "8-1-16-16-25 14-15-23, 1-18-9-5-12?"
print(a1z26(mensaje))
print()


mensaje = "5-19-23-6-21-16 18-9-6 4-16-19 22-12-15-10-20-19-25-19"
print(combined(mensaje))
print()


mensaje = "18-23-20-19-20 8-15-21-4-3-6-19-5 22-12-19-23-21-16-19-20 22-25 5-3-10"
print(combined(mensaje))


mensaje = "4-16-19 4-23-12-19'5 4-9-12-20, 4-16-19 5-3-11-11-19-6'5 20-9-10-19"
print(combined(mensaje))
print()


mensaje = "15-10 11-19-11-9-6-15-19-5 4-16-19 8-15-10-19-5 5-4-15-12-12 8-12-23-25"
print(combined(mensaje))
print()
