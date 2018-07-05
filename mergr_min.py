# 链接：https://www.nowcoder.com/questionTerminal/c5b6217d35a047a6a7effdd5724abe22
# 来源：牛客网

def smallestNumber(numList):
    strList = [str(num) for num in numList]
    for i in range(0,len(strList)):
        minIndex = i
        for j in range(i+1,len(strList)):
            if strList[j][0] < strList[minIndex][0]:
                minIndex = j
                strList[i], strList[minIndex] = strList[minIndex], strList[i]
    smallNumber = ''.join(strList)
    return smallNumber

def get_final_words():
    s = input()
    string = s.split(' ')
    print(len(string[-1]))

def get_numbeof_word():
    s = input()
    string = s.split(' ')
    A = ''
    B = string[-1]
    count = 0
    for i in range(len(string)-1):
        A += string[i]
    for j in range(len(A)):
        if A[j] == B or A[j] == B.lower():
            count += 1
    print(count)

def get_sorted_list():
    n = int(input())
    inputArray = []
    for i in range(n):
        inputArray.append(int(input()))
    inputArray = list(set(inputArray))
    inputArray.sort()
    for num in inputArray:
        print(num)

def del_string_by_eight():
    inputString = []
    inputString.append(input())
    inputString.append(input())
    for string in inputString:
        n = len(string) % 8
        print(n)
        if n:
            for i in range(8-n):
                string += '0'
        print(string)
        while string:
            print(string[0:8])
            string = string[8:]
            print(string)


# print(smallestNumber([13,2,12,3,4,5]))
# get_final_words()
# get_numbeof_word()
# get_sorted_list()
del_string_by_eight()