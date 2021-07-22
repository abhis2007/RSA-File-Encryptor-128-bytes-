import math


def getPublicKey(phi_n):
    publicKey = 2
    while publicKey:
        if math.gcd(publicKey, phi_n) == 1:
            break
        publicKey += 1
    return publicKey
