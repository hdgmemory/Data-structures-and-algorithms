# 二进制表示中，最后的那个1被减去后，低位都变为0，高位不变，按位与就可以去掉这个1
def num_of_1(n):
    ret = 0
    while n&0xffffffff:
        ret += 1
        n = n & n-1
    return ret
print(num_of_1(-8))

# def NumberOf1(n):
#     # if n >= 0:
#     #     return bin(n).count('1')
#     # else:
#         return bin(n & 0xffffffff).count('1')
#
# print(NumberOf1(3))
# print(bin(-10))