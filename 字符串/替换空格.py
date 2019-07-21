#时间复杂度哦O(n)
def replaceSpace(s):

    p1 = len(s) - 1
    res = list(s)
    n = s.count(' ')
    res += [0] * n * 2
    p2 = len(res) - 1
    while p1 != p2:
        if res[p1] == ' ':
            res[p2] = '0'
            res[p2 - 1] = '2'
            res[p2 - 2] = '%'
            p2 -= 3
        else:
            res[p2] = res[p1]
            p2 -= 1
        p1 -= 1
    return ''.join(res)

s = "hello world a."
r = replaceSpace(s)
print(r)
