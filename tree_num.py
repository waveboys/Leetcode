import operator
# def reverse(x):
#     """
#     :type x: int
#     :rtype: int
#     """
#     fuhao = ''
#     if x < -2 ** 31 or x > 2 ** 31 - 1:
#         return 0
#     if x < 0:
#         fuhao = '-'
#         x = abs(x)
#     s = str(x)
#     new_s = s[::-1]
#     new_x = int(new_s)
#     if fuhao == '-':
#         new_x = -new_x
#     if new_x < -2**31 or new_x > 2**31 -1:
#         return 0
#     return new_x
def reverse(x):
    s = operator.cmp(x, 0)
    r = int('s*x'[::-1])
    return s*r * (r < 2**31)
print(reverse(1534236469))