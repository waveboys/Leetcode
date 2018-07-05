def myAtoi(str):
    numStrs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    fuhao = ['+', '-']
    mystr = str.strip()
    result = ''
    my_fuhao = ''
    if mystr == '':
        return 0
    if mystr[0] not in numStrs and mystr[0] not in fuhao:
        return 0
    if mystr[0] in fuhao:
        if len(mystr) == 1:
            return 0
        if mystr[1] not in numStrs:
            return 0
        else:
            my_fuhao = mystr[0]
    else:
        result += mystr[0]


    for i in range(1, len(mystr)):

        if mystr[i] in numStrs:
            result += mystr[i]
        else:
            break
    if my_fuhao == '-':
        num = -int(result)
    else:
        num = int(result)
    return num

print(myAtoi('  1-2'))

