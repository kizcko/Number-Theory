import random
def jacobi_symbol(a, n):
    if (n % 2 == 0): #n impar
        return 0
    t = 1
    while a != 0:
        while a % 2 == 0:
            #multiplii de 2
            a = a // 2
            if (n % 8 == 3) or (n % 8 == 5):
                t = -t
        #legea reciprocitatii
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            t = -t
        a = a % n
    if n == 1:
        return t
    else:
        return 0

def strassen(n, k):
    for i in range(k):
        a = random.randint(2, n-2)
        x = jacobi_symbol(a, n)
        if x == 0 or pow(a, (n-1) // 2, n) != (x % n):
            return "Compus"
    return "Prim"


# print(jacobi_symbol(7,3))

iterations = 50
num = 15

print(strassen(num,iterations))
