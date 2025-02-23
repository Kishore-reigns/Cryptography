def extended_euclidean(a,b):
    a1 , a2 , a3 = 1 , 0 , a
    b1 , b2 , b3 = 0 , 1 , b
    while (True):
        if b3 == 0:
            print("multiplicative inverse doesn't exist since a and b are not relatively prime")
            return None
        elif b3 == 1:
            return b2%b
        q = a3 // b3 
        t1 , t2 , t3 = a1 - q*b1 , a2 - q*b2 , a3 - q*b3
        a1 , a2 , a3 = b1 , b2 , b3
        b1 , b2 , b3 = t1 , t2 , t3

def extended_euclidean_verbose(a,b):
    a1 , a2 , a3 = 1 , 0 , a
    b1 , b2 , b3 = 0 , 1 , b
    q = 0 
    t1 , t2 , t3 = 0 , 0 , 0
    print("q\ta1\ta2\ta3\tb1\tb2\tb3\tt1\tt2\tt3")
    print(q,"\t",a1,"\t",a2,"\t",a3,"\t",b1,"\t",b2,"\t",b3,"\t",t1,"\t",t2,"\t",t3)
    while (True):
        if b3 == 0:
            print("multiplicative inverse doesn't exist since a and b are not relatively prime")
            break
        elif b3 == 1:
            b2 = b2 % b
            print("Multiplicative inverse = ",b2)
            break
        q = a3 // b3 
        t1 , t2 , t3 = a1 - q*b1 , a2 - q*b2 , a3 - q*b3
        
        a1 , a2 , a3 = b1 , b2 , b3
        b1 , b2 , b3 = t1 , t2 , t3
        print(q,"\t",a1,"\t",a2,"\t",a3,"\t",b1,"\t",b2,"\t",b3,"\t",t1,"\t",t2,"\t",t3)
        

if __name__ == "__main__":
    a = int(input("Enter a = "))
    b = int(input("Enter b = "))
    extended_euclidean_verbose(a,b)
    print(extended_euclidean(a,b))
