##递归，
class Node():
    def __init__(self, x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right


class Solution():
    def isBalanced(self, root):
        if root == None:
            return 0
        leftheight = self.isBalanced(root.left)
        rightheight = self.isBalanced(root.right)
        if leftheight >= rightheight:
            return leftheight + 1
        else:
            return rightheight + 1


if __name__ == '__main__':

    #root = Node('D', Node('B', Node('A'), Node('C')), Node('E', Node('G', Node('F'))))
    root = Node('D', Node('B', Node('A',Node('C'))))
    s = Solution()
    print(s.isBalanced(root))