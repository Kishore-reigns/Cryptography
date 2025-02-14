def encrypt(p,key):
    c = ""
    for i in p :
        #if i.isalpha() :
            #base = ord('A') if i.isupper() else ord('a')
        c += chr( ord(i) + key)
        #else:
           # c += i  
    return c
def decrypt(c,key):
    p = ""
    for i in c :
        #if i.isalpha():
            #base = ord('A') if i.isupper() else ord('a')
        p += chr(ord(i) -key)
        #else:
         #   p += i 
    return p


if __name__ == "__main__":
    print("Here we are performing shift cipher((shifts only letters) to encrypt and decrypt plain texts !! \n")
    print("1.Encrypt\n2.Decrypt\n")
    ch = int(input("Enter your Choise : "))
    if(ch == 1):
        p = input("Enter the plaintext : ")
        key = int(input("Enter key : "))
        c = encrypt(p,key)
        print("plain text : ",p,"\nkey : ",key, "\ncipher text : ", c)
    elif(ch == 2) :
        c = input("Enter the cipher text you want to decrypt :")
        key = int(input("Enter the key : "))
        p = decrypt(c,key)
        print("cipher text : ",c,"\nkey : ",key, "\nplain text : ", p)
    else :
        print("Wrong choise !")
