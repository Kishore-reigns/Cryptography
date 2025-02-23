import random
import string
import binascii
random_key = ""

def setRandomkey(plaintext):
    key = ""
    for i in range(len(plaintext)):
        if plaintext[i] != ' ':
            key += random.choice(string.ascii_letters + string.digits)
        else :
            key += ' ' 
    return key 

def encrypt(plaintext,key):
    res = []
    print(key)
    for i in range(len(plaintext)):
         if plaintext[i] != ' ':
            value = (ord(plaintext[i]) ^ ord(key[i]))
            res.append(value)
         else:
             res.append(32)
    
    #print( binascii.hexlify(res).decode() )
    # res, binascii.hexlify(res) , binascii.hexlify(bytearray(res)) , binascii.hexlify(res).decode() , binascii.hexlify(bytearray(res)).decode() , bytearray(res)
    return binascii.hexlify(bytearray(res)).decode()

def decrypt(ciphertext, key):
    res = ""
    try:
        byte = bytearray(binascii.unhexlify(ciphertext))
    except:
        return "inavalid cipher"
    for i in range(len(byte)):
        if key[i] != ' ':
            res += chr(byte[i] ^ ord(key[i]))
        else:
            res += ' '
    
    return res

if __name__ == "__main__":
    print("1.random_key encryption ( key will be genearted automatically ) \n2. Decryption \nother keystroke -> quit")
    while(True):
        ch = int(input("Enter choise : "))
        if(ch == 1):
            plaintext = input("Enter the plaintext : ")
            random_key = setRandomkey(plaintext)
            print(f"Random key => {random_key}")
            ciphertext = encrypt(plaintext,random_key)
            print(f"cipher text =>{ciphertext}")
        elif(ch == 2):
            if not random_key :
                print("random key is not generated yet")
                continue 
            ciphertext = input("Enter the ciphertext (We got the key) : ")
            plaintext = decrypt(ciphertext,random_key)
            random_key = ''
            print(plaintext)
        else : 
             break ; 