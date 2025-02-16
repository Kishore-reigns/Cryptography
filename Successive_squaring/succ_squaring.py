# n = 38 
# while( p <= n):
#     ans = (n&p)
#     print(ans)
#     p = p << 1

def findMod(a,k,b):
    res = 1
    temp = a % b
    while( k > 0 ):
        if( k%2 == 1):
            res = (res * temp) % b 
        temp = (temp * temp) % b
        k //= 2
    return res%b


if __name__ == "__main__":
    a = int(input("Enter Base : "))
    k = int(input("Enter Exponent : "))
    b = int(input("Enter Mod : "))
    print("Result  = ", findMod(a,k,b))