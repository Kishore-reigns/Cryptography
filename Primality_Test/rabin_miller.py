
def rabin_miller(n):
    m = find_m(n-1)
    print(m)
    a = 2 # can be chose from 1 < a <= n-1 
    b = a**m % n 

   
    while(b != 1 and b != -1):
        b = b**2 % n 
    if(b == 1):
        return False
    return True


    
def find_m(n):
    i , m = 0 , 0 
    while( n%(2**i) == 0 ):
        m = n/2**i
        i += 1
    return m


if __name__ == '__main__':
    n = int(input("Enter the number : "))
    if(rabin_miller(n)):
        print("The given number has the probabilty to be prime number")
    else:
        print("The given number has no probabilty to be a prime number")