#递归
class Solution():
    def chongjian(self, pre, tin):
        if len(pre)==0 | len(tin)==0:
            return None

        root = TreeNode(pre[0])
        for order,item in enumerate(tin):
            if root .val == item:
                root.left = self.chongjian(pre[1:order+1], tin[:order])
                root.right = self.chongjian(pre[order+1:], tin[order+1:])
                return root

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

if __name__ == '__main__':
    solution = Solution()
    preorder_seq = [1,2,4,7,3,5,6,8]
    midorder_seq = [4,7,2,1,5,3,8,6]
    treeRoot = solution.chongjian(preorder_seq, midorder_seq)
    print(treeRoot.val,treeRoot.left.val,treeRoot.right.val)