
def fermat_test(p):
    for a in range(1,p):
        if( ( (a**p) - a) % p != 0 ):
            return False
    return True

if __name__ == "__main__":
    p = int(input("Enter the number : "))
    print(fermat_test(p))