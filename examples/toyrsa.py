from petlib.bn import Bn
from os import urandom

def gen_key():
    """Example naive RSA key generation"""
    p = Bn.get_prime(512)
    q = Bn.get_prime(512)
    m = p * q
    phi = (p - 1) * (q - 1)
    e = Bn(2**16 + 1)
    d = e.mod_inverse(phi)
    pub = (e, m)
    priv = (d,)
    return pub, priv

def enc(pub, plaintext):
    """Naive RSA encryption"""
    e, m = pub
    plain = Bn.from_binary(plaintext)
    assert 1 < plain < m
    cipher = pow(plain, e, m)
    return cipher.binary()

def dec(pub, priv, ciphertext):
    """Naive RSA decryption"""
    _, m = pub
    d, = priv
    cipher = Bn.from_binary(ciphertext)
    assert 1 < cipher < m
    plain = pow(cipher, d, m)
    return plain.binary()

if __name__ == "__main__":
    pub, priv = gen_key()
    c = enc(pub, "Hello World!")
    p = dec(pub, priv, c)
    assert p == "Hello World!"
    print p

    