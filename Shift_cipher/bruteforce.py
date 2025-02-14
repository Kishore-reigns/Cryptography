from shiftCipher import decrypt

c = input("Enter the cipher text : ")
keysize = int(input("Enter the largest key (works fine till 54): "))

for i in range(1,keysize+1) :
    print("key : ", i , "plain text : ", decrypt(c,i))
