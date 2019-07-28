####https://www.nowcoder.com/ta/coding-interviews?query=&asc=true&order=&page=1
####牛客网题目

def StrToInt(s):
    res, mult, flag = 0, 1, 1
    if not s:
        return res
    if s[0] == '-' or s[0] == '+':
        if s[0] == '-':
            flag = -1
        s = s[1:]
    for i in range(len(s) - 1, -1, -1):
        if '9' >= s[i] >= '0':
            res += (ord(s[i]) - 48) * mult
            mult = mult * 10
        else:
            return 0
    return res * flag


s = StrToInt('-123')
print(s)
print(type(s))
