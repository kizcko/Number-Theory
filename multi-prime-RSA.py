import sys
import sympy
import time

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
def generate_numar_prim(*args):
    nr = sympy.randprime(pow(2, 512), pow(2, 523))
    while nr in args:
        nr = sympy.randprime(pow(2, 512), pow(2, 523))
    return nr
def write_to_file(path='', content=''):
    with open(path, "w") as fd:
        fd.write(str(content))
# https://www.geeksforgeeks.org/using-chinese-remainder-theorem-combine-modular-equations/
def solve_crt(m, x):
    while True:
        temp_m = sympy.mod_inverse(m[1], m[0]) * x[0] * m[1] + sympy.mod_inverse(m[0], m[1]) * x[1] * m[0]
        temp2_m = m[0] * m[1]

        x.remove(x[0])
        x.remove(x[0])
        x = [temp_m % temp2_m] + x

        m.remove(m[0])
        m.remove(m[0])
        m = [temp2_m] + m

        if len(x) == 1:
            break

    return x[0]
def decrypt_message_crt(p,q,r,n,e,d, m,):
    start = time.time()
    m1 = pow(m % p, d % (p - 1), p)
    m2 = pow(m % q, d % (q - 1), q)
    m3 = pow(m % r, d % (r - 1), r)
    solve = solve_crt([p, q, r], [m1, m2, m3])
    end = time.time() - start
    return solve,end
def generare_mesaj_criptat(mesaj, n=0, e=0):
    criptare = pow(mesaj, e, n)  # m ** e % n
    write_to_file("encrypted.txt", criptare)
    return criptare
def decriptare(y, d, n):
    start = time.time()
    x = pow(y, d, n) # y ** d % 0n
    end = time.time() - start
    return x, end

def multiprime_RSA():
    average_time = 0

    p = generate_numar_prim()
    q = generate_numar_prim(p)
    r = generate_numar_prim(p,q)

    n = p * q * r
    e = pow(2, 16) + 1

    public_key = (n, e)
    print("Public_key:",public_key)
    phi_n = (p - 1) * (q - 1) * (r - 1)
    k = gcd(e, phi_n)

    d = sympy.mod_inverse(e, phi_n)
    print("Private_key:", d)

    message = 1234
    y = generare_mesaj_criptat(message, n, e)
    x_decrypt_CRT, time_CRT = decrypt_message_crt(p, q, r, n, e, d, y)
    print("\nDecrypted message CRT: ",x_decrypt_CRT)
    print("Timp: ", time_CRT)

    x_decrypt,time= decriptare(y, d, n)
    print("\nDecrypted message: ",x_decrypt)
    print("Timp: ", time)

    average_time += time / time_CRT
    print("\nTimp average intre cele 2: ", average_time)

multiprime_RSA()