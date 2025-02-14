from shiftCipher import decrypt

c = input("Enter the cipher text : ")
keysize = int(input("Enter the largest key : "))

for i in range(1,keysize+1) :
    print("\nkey : ", i , "plain text : ", decrypt(c,i))
