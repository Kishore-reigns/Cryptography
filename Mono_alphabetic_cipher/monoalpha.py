predefined_key = "mrjocktvquizphdbagsfewlynx"
custom_key = None
hashmap = {}

def isvalid_custom_key(key): 
    global hashmap
    if(len(key) != 26):
        print("key is not 26 chars long")
        return None
    for i in key :
        if i in hashmap:
            hashmap = {}
            print("repeated characters not allowed, all chars must be unique")
            return None
        else :
             hashmap[i] = 1
    return key

def encrypt(plaintext , key):
    res = ""
    for i in plaintext.lower():
        if i.isalpha(): 
            res += key[ord(i)-ord('a')]
        else :
            res += i 
    return res

def decrypt(ciphertext , key):
    res = ""
    for i in ciphertext.lower():
        if i.isalpha():
            res += chr(key.index(i) + ord('a'))
        else : 
            res += i 
    return res 
     

if __name__ == "__main__":
    print("1.predefined key encryption \n2.custom_key for encryption \n3.predefined key decryption \n4.customkey decryption\n5.set custom key\nother key -> quit")
    while(True):
        ch = int(input("Enter choise : "))
        if(ch == 1):
            plaintext = input("Enter the plaintext : ")
            ciphertext = encrypt(plaintext,predefined_key)
            print(ciphertext)
        elif(ch == 2):
                if custom_key is not None:
                    plaintext = input("Enter the plaintext : ")
                    ciphertext = encrypt(plaintext,custom_key)
                    print(ciphertext)
                else :
                    print("custom key is not set")
        elif(ch == 3):
            ciphertext = input("Enter the ciphertext : ")
            plaintext = decrypt(ciphertext,predefined_key)
            print(plaintext)
        elif(ch == 4):
                if custom_key is not None :
                     ciphertext = input("ENter the ciphertext : ")
                     plaintext = decrypt(ciphertext,custom_key)
                     print(plaintext)
                else :
                     print("custom key is not set")
        elif(ch == 5):
            key = input("Enter custom key : ")
            if(isvalid_custom_key(key)):
                 custom_key = key
                 print("custom key set successfully ")
            else :
                 print("custom key set failed ")
        else : 
             break ; 

    
