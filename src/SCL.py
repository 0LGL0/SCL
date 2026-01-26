def calculate(noSpacesStr):
    noSpacesStr = noSpacesStr.replace(" ", "")
    i = 0
    arr = list()
    numStr = ""
    while i < len(noSpacesStr):
        c = noSpacesStr[i]
        if c.isdigit() or c == ".":
            numStr += c
        else:
            arr.append(numStr)
            arr.append(c)
            numStr = ""
        i += 1
    arr.append(numStr)
    i = 1

    while i < len(arr) - 1:
        left = arr[i - 1]
        mid = arr[i]
        right = arr[i + 1]

        divMulRes = 0
        if mid in "*/":
            if mid == "*":
                divMulRes = float(left) * float(right)
            else:
                divMulRes = float(left) / float(right)

            arr.pop(i + 1)
            arr.pop(i)
            arr.pop(i - 1)
            arr.insert(i - 1, divMulRes)
            i -= 1

        i += 1
    i = 0

    res = float(arr[0])
    while i < len(arr):
        if arr[i] == "+":
            res += float(arr[i + 1])
        elif arr[i] == "-":
            res -= float(arr[i + 1])
        i += 1

    return res


res = calculate("3+5*2*2")
print(res)
