import time
import sympy


def save_encrypted_content(encrypted_text):
    with open("encryptedMPowerRSA.txt", "w") as fd:
        fd.write(str(encrypted_text))
def get_encrypted_file(mesaj, n, e):
    encrypted_text = pow(mesaj, e, n)
    save_encrypted_content(encrypted_text)
    return encrypted_text
def decriptare(y, d, n):
    start = time.time()
    x = pow(y, d, n)
    end = time.time() - start
    return x,end
def decriptare_hensel(y, d, p, q, e):
    start = time.time()
    mq = pow(y % q, d % (q - 1), q)

    m0 = pow(y % p, d % (p - 1), p)
    m1 = (((y - pow(m0, e, p * p)) // p) * sympy.mod_inverse(e * pow(m0, e - 1, p), p)) % p
    mp2 = m1 * p + m0
    x = mp2

    alpha = (((mq - x) % q) * sympy.mod_inverse(mp2, q)) % q
    x += alpha * mp2

    end = time.time() - start
    return x, end

def multiprimeRSA():
    average_time = 0
    p = q = sympy.randprime(pow(2, 512), pow(2, 523))
    while p == q:
        q = sympy.randprime(pow(2, 512), pow(2, 523))

    n = p * p * q
    phi_n = p * (p - 1) * (q - 1)
    e = pow(2, 16) + 1
    d = sympy.mod_inverse(e, phi_n)
    mesaj = 12345
    y = get_encrypted_file(mesaj, n, e)

    public_key = (n, e)
    print("Public_key:", public_key)
    x_decrypt, time = decriptare(y, d, n)
    print("\nDecrypted message: ", x_decrypt)
    print("Timp: ", time)
    x_decryptHensel,time_Hensel = decriptare_hensel(y, d, p, q, e)
    print("\nDecrypted message: ", x_decryptHensel)
    print("Timp: ", time_Hensel)

    average_time += time / time_Hensel
    print("\nTimp average intre cele 2: ", average_time)

multiprimeRSA()