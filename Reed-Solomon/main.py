import decoding
from encoding import encoding
from decoding import *

m = 29
p = 11
s = 1
k = 3


def convert_to_ascii(text):
    return "".join(str(ord(char)) for char in text)



if isinstance(m, str):
    m = int(convert_to_ascii(m))

def main(m,p,s,k):
    print("\nEncoding\n",20*'=')
    print('\nm:', m)
    initial = encoding(m, p, s, k)
    print("\n\nDecoding\n", 20 * '=')
    z = generate_z(initial,p)
    print("\nZ:",z)
    polynomial(p, z, k,s,initial)

main(m,p,s,k)