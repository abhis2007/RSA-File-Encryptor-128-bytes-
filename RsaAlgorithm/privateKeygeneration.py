def genPrivateKey(publicKey,phi_n):
    k = 1
    privateKey = (k * phi_n) + 1
    while privateKey % publicKey != 0:
        k += 1
        privateKey = (k * phi_n) + 1
    return privateKey // publicKey