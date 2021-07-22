def readfile(fName):
    lists = []
    with open(fName + ".txt", "r") as file:
        ln = len(file.read())
        i = 0
        file.seek(0)
        while i <= ln:
            ct = file.read(1)

            lists.append(ct)
            i = file.tell()+1
    file.close()

    return lists

