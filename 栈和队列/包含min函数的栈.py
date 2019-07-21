class Stack:
    """
    用列表表示栈，符合先进后出的原则
    用两个栈解决：
    第一个栈stack正常出入栈
    第二个support_stack每次push时，将stack中的最小值push进去，而不是直接push某一个值
    每次pop操作，两个栈都进行pop,
    这样support_stack[-1]表示当前stack的最小值
    """

    def __init__(self):
        self.stack = []
        self.support_stack = []
        # min_num其实可以不要，用support_stack[-1]表示即可
        self.min_num = None

    def push(self, num):
        self.stack.append(num)
        if self.min_num is None:
            self.min_num = num
            self.support_stack.append(self.min_num)
        elif self.min_num < num:
                self.support_stack.append(self.min_num)
        else:
            self.min_num = num
            self.support_stack.append(num)

    def pop(self):
        if self.stack:
            self.support_stack.pop()
            return self.stack.pop()
        return

    def min(self):
        return self.support_stack[-1]


