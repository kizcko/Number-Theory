import numpy as np

message = np.array([], object)

# m = 29
# p = 11
# s = 1
# k = 4


def input_vector(m, p, k):
    k1 = k
    k -= 1
    global message
    message = np.array([], object)
    message = np.append(message, 0)
    a = m
    while a > 0:
        a = m // p
        b = m % p
        m = a
        message = np.append(message, b)
        k -= 1
        if k == 1 and a != 0:
            message = np.append(message, a)
            break

    if message.shape[0] < k1:
        for i in range(1, k + 1):
            message = np.insert(message, 0, 0, axis=0)

    print("Vector: ", message)


def horner(a, x):
    result = 0
    for i in range(len(a) - 1, -1, -1):
        result = a[i] + (x * result)

    return result


def polynomial(p, s, k):
    n = k + 2 * s
    y = np.array([], object)
    for i in range(1, n + 1):
        y = np.append(y, (horner(message, i) % p))
    print("Polinom: ", y)
    return y


def encoding(m, p, s, k):
    input_vector(m, p, k)
    y = polynomial(p, s, k)
    return y

# encoding(m, p, s, k)
# array([9, 0, 6, 5, 8])
