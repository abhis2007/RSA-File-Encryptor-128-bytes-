import random
import publicKeyGeneration
import privateKeygeneration
import filereading

primeLength = 10001
prime = [1] * primeLength
first_primes_list = []


def sieve():
    prime[1] = 0
    prime[0] = 0
    i = 2
    while i ** 2 <= primeLength:
        if prime[i]:
            for j in range(i * i, primeLength, i):
                prime[j] = 0
        i = i + 1
    for i in range(2, primeLength):
        if prime[i]: first_primes_list.append(i)


def genRandomPrime(n):
    return random.randrange(2 ** (n - 1) + 1, 2 ** n - 1)


def lowLevelPrimality(n):
    while True:
        primeCandidate = genRandomPrime(n)
        for genPrime in first_primes_list:
            if primeCandidate % genPrime == 0 and primeCandidate >= genPrime ** 2:
                break
            else:
                return primeCandidate


def isComposite(primeRoundTester, primeCandidate):
    d = primeCandidate - 1
    divisible2 = 0
    while d % 2 == 0:
        d >>= 1
        divisible2 += 1
    if pow(primeRoundTester, d, primeCandidate) == 1:
        return False
    for i in range(divisible2):
        if pow(primeRoundTester, 2 ** i * d, primeCandidate) == primeCandidate - 1:
            return False
    return True


def checkPrime_milerTest(primeCandidate):
    millerTestRound = 2
    for i in range(millerTestRound):
        primeRoundTester = random.randrange(2, primeCandidate)
        if isComposite(primeRoundTester, primeCandidate):
            return False
    return True


sieve()


def generatePrime():
    while 1:
        p = lowLevelPrimality(500)
        if not checkPrime_milerTest(p):
            continue
        else:
            return p


def convertBinToDecimal(binary):
    ans = 0
    bitPos = 0
    while binary:
        if binary % 10:
            ans += pow(2, bitPos)
        binary //= 10
        bitPos += 1
    return ans


p = generatePrime()
q = generatePrime()

n = p * q

phi_n = (p - 1) * (q - 1)

public_key = publicKeyGeneration.getPublicKey(phi_n)

print("public_key", public_key)

'''sending n and public key over any network'''

private_key = privateKeygeneration.genPrivateKey(public_key, phi_n)

print("private_key", private_key)
n = p * q
# print(n)
print("1 For encryption other than 1 for decryption")
op = int(input())
if op == 1:
    lists = filereading.convertIntoInt("originalText")
    key = open("privateKey.txt", "w")
    key.write(str(private_key))
    key.close()
    val_n = open("nValue.txt", "w")
    val_n.write(str(n))
    key.close()
    file = open("cipherText.txt", "w+")
    for i in lists:
        asciiCode = filereading.convertBinToDecimal(i)
        cipher_text = pow(asciiCode, public_key, p * q)
        file.write(str(cipher_text) + " ")
    file.close()
if op == 2:
    print("Provide Private Key")
    private_key = int(input())
    print("Provide value of N")
    n = int(input())
    output = open("plainTextDecrypted.txt", "w")
    print("-----Wait while we decrypt your treasure.-----")
    with open("cipherText.txt", "r") as file:
        content = file.read()
        cipher_text_string = ""
        plain_text_string = ""
        for i in content:
            if i != " ":
                cipher_text_string += i
            else:
                cipher_text = int(cipher_text_string)
                plain_text = chr(pow(cipher_text, private_key, n))
                cipher_text_string = " "
                if plain_text == " ":
                    output.write(plain_text_string + " ")
                    plain_text_string = ""
                else:
                    plain_text_string += plain_text
        output.write(plain_text_string)
    file.close()
    output.close()
    print("----- Decrypted successfully no one has seen your treasure.-----")
# for decypting and data which encrypted earlier should be used same public key only
