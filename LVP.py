def longestValidParenthess(s):
    stack = []
    step = [0 for i in range(len(s))]
    for i, c in enumerate(s):
        if c == '(':
            stack += [i]
        elif len(stack) > 0:
            j = stack.pop(-1)
            step[j] = 1
            step[i] = 1

    count = 0
    max_len = 0
    for k in step:
        if k == 1:
            count += 1
            if count > max_len:
                max_len = count
        else:
            count = 0
    print(step)
    return max_len

print(longestValidParenthess('((()())'))
