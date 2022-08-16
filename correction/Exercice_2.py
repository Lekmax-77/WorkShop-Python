def exerciseTwo(nb):
    string = str(nb)
    result = [c for c in string]
    count = 0

    for i in range(len(string) - 1): # stuck in array the multiplication of the actual digit and is neighboor
        mult = int(string[i]) * int(string[i + 1])
        result.append(str(mult))

    mult = int(string[0])
    for i in range(1, len(string)): # stuck in array the mutiplication of all digits
        mult *= int(string[i])
    result.append(str(mult))

    is_colorful = "false" if len(result) != len(set(result)) else "true"
    # print(nb, "-->", is_colorful)

# exerciseTwo()