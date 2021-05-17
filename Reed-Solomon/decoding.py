import random
import itertools
import numpy as np
from egcd import egcd

# initial = [9, 0, 6, 5, 8]
# z = [9, 2, 6, 5, 8]
# k = 3
# s = 1
# p = 11


def generate_z(initial,p):
    z = initial.copy()
    i =  np.random.randint(0, high=len(z))
    new_number = np.random.randint(50) %p
    z[i] = new_number
    return z

def fc(p, z, k, s,initial):
    # generate A
    n = k + 2 * s
    n1 = np.arange(1, n+1)
    for i in (n1-1):
        if z[i] != initial[i]:
            n1 = np.delete(n1,i)

    # print(n1)
    list_subsets = np.array([set(i) for i in itertools.combinations(n1, k)])
    A = np.random.choice(list_subsets)
    # print("Submultimea A:",A)
    # compute fc
    fc = 0
    for i in A:
        prod = 1
        b = set(A)
        b.remove(i)
        for j in b:
            prod = prod * j * (egcd((j - i) % p, p)[1] % p)
        fc = fc + z[i-1] * prod
    fc = fc % p
    return fc, A

#https://www.geeksforgeeks.org/vietas-formulas/
def vietaFormula(roots):
    n = len(roots)
    coeff = [0] * (n + 1)
    coeff[n] = 1
    for i in range(1, n + 1):
        for j in range(n - i - 1, n):
            coeff[j] = coeff[j] + (-1) * roots[i - 1] * coeff[j + 1]

    coeff = coeff[::-1]
    return coeff


def polynomial(p, z, k,s,initial):
    fc1, A = fc(p, z, k, s,initial)
    print("A: ",A)
    m = [0] * len(A)
    if fc != 0:
        roots2 = [0] * len(A)
        for i in A:
            test = np.array([])
            prod = 1
            b = set(A)
            b.remove(i)
            for j in b:
                prod = prod * (i - j)
            prod = egcd(prod % p, p)[1] % p

            roots = vietaFormula(list(b))

            roots = list(map(lambda x: x * z[i-1] * prod, roots))

            for i in range(0, len(A)):
                m[i] = m[i] + roots[i]
        message = np.array([])
        for i in m:
            message = np.append(message,i%p)
        print(message)







