from shiftCipher import decrypt

c = input("Enter the cipher text : ")

for i in range(1,26) :
    print("\nkey : ", i , "plain text : ", decrypt(c,i))
