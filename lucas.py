

def generate_Mersenne(s):
    return pow(2,s)-1


def efficient(s,n,mersenne):
    print("\ns:",s)
    s1 = divmod(s, pow(2, n))  # A=A1*2^n+A0
    print(s1[0], s1[1])

    if s1[0] == mersenne or s1[1] == mersenne:
        print("return 0")
        return 0
    if s1[0] + s1[1] < mersenne:
        return (s1[0] + s1[1])
    else:
        s2 = s1[0] + s1[1] - mersenne
        print("s2 = ",s2)
        if s2 >= mersenne:
            return efficient(s2, n, mersenne)
        else:
            return s2



def lucasTest(n):
    mersenne = generate_Mersenne(n)
    print(mersenne)
    mp.insert(len(mp), s[-1])
    while len(s) <= n-2:
        s.insert(len(s), s[-1]**2 - 2)
        valoare = efficient(s[-1],n,mersenne)
        mp.insert(len(mp), valoare)

    print(mp)
    if(mp[-1]==0 ):
        print("\nM-",n ," este prim",sep="")
    else:
        print("\nM-", n, " nu este prim", sep="")


s=[4]  #secventa lucas-lehmer
mp=[]

lucasTest(11)


def lucas_lehmer(p):
    M = 2 ** p - 1
    s = 4
    for _ in range(p - 2):
        s = (s * s - 2) % M
        print(s)

# lucas_lehmer(5)