#方法一
class Solution():
    def Power(self, base, exponent):
        if exponent < 1:
            return 1 / self.getPower(base, -exponent)
        else:
            return self.getPower(base, exponent)

    def getPower(self, base, exponent):
        if base == 0:
            return 0
        elif exponent == 1:
            return base
        res = 1
        for i in range(exponent):
            res *= base
        return res
s = Solution()
print(s.Power((2),2))


#方法二
class Solution():
    def Power(self, base, exp):
        if exp < 1:
            return 1 / self.getPower(base, -exp)
        else:
            return self.getPower(base, exp)
    def getPower(self, base, exp):
        if exp == 0:
            return 1
        elif exp == 1:
            return base
        res = self.Power(base, exp >> 1)
        res *= res
        if exp & 1 == 1:
            res *= base
        return res
s = Solution()
print(s.Power(3,2))
