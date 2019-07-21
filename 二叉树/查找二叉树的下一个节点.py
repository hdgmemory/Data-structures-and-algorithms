#思想：使用中序遍历找出下一个节点，如果该节点有右子树，则下一个节点是最下面的左子树，否则判断该节点是否是父节点的左节点
#如果是则输出，否则继续往上找，直到找到为止。

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return None
        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        else:
            while pNode.next:
                if pNode == pNode.next.left:
                    return pNode.next
                pNode = pNode.next
        return None
