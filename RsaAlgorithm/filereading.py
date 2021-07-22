def binary(n):
    bits = 0
    lists = []
    while bits <= 7:
        mask = 1 << bits
        p = 0
        if n & mask:
            p = 1
        lists.append(str(p))
        bits += 1
    lists.append('1')
    lists.reverse()
    binaryVal = int("".join(lists))
    return binaryVal


def convertBinToDecimal(n):
    decimal = 0
    bitCount = 0
    n %= pow(10, 8)
    # print(n)
    while n != 0:
        mask = 1 << bitCount
        if n % 10:
            decimal += mask
        bitCount += 1
        n //= 10
    return decimal


def convertIntoInt(fileName):
    lists = []
    with open(fileName + ".txt", "r+") as file:
        ln = len(file.read())
        file.seek(0)
        i = 0
        while i < ln:
            content = file.read(1)
            lists.append(binary(ord(content)))
            i += 1
    return lists
