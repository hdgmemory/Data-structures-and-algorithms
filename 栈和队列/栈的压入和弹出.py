##借用辅助栈实现
class Solution():
    def IsPopOrder(self, pushV, popV):
        stack = []
        while popV:
            if stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
            elif pushV:
                stack.append(pushV.pop(0))
            else:
                return False
        return True
