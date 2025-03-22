import random 

def rabin_miller(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    k =5
    m ,r = find_m_and_r(n-1)
    #print(m)
    for _ in range(k):
        a = random.randint(2,n-2) 
        #a = 2 
        b = pow(a, m, n)  # Compute a^m % n
        if(b== n-1 or b == 1):
            continue
        for _ in range(r-1):
            b = pow(b,2,n)
            if b == n -1:
                break
        else:
            return False
    return True
            


    
def find_m_and_r(n):
    """Find m and r such that n-1 = m * 2^r, where m is odd."""
    r = 0
    while n % 2 == 0:
        n //= 2
        r += 1
    return n, r



if __name__ == '__main__':
    n = int(input("Enter the number : "))
    if(rabin_miller(n)):
        print("The given number has the probabilty to be prime number")
    else:
        print("The given number has no probabilty to be a prime number")