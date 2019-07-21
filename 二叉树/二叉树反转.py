#也叫二叉树的镜像
#递归实现
class Node():

    def __init__(self, value=None, left=None, right=None):

        self.value = value

        self.left = left  # 左子树

        self.right = right  # 右子树

def invertTree(root):
    if root == None:
        return None
    temp = root.left
    root.left = root.right
    root.right = temp
    print(root.value)
    invertTree(root.left)
    invertTree(root.right)


if __name__ == '__main__':
    root = Node('4', Node('2', Node('1'), Node('3')), Node('7', Node('6'), Node('9')))
    invertTree(root)

















