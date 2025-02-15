def euclidean_gcd(a,b):
    if b == 0 :
        return a
    return euclidean_gcd(b,a%b)

def euclidean_gcd_verbose(a,b):
    if b == 0 :
        return a 
    print("a = ",a,"b = ",b,"r = ", a%b)
    return euclidean_gcd_verbose(b,a%b)


if __name__ == "__main__":
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    print("GCD ",euclidean_gcd(a,b))
    print(euclidean_gcd_verbose(a,b))