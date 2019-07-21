# https://www.cnblogs.com/shunyu/p/4986288.html   参考文档
#https://www.cnblogs.com/qiaojushuang/p/7822066.html    python剑指offer
###B-树和B+树       https://www.jianshu.com/p/8b653423c586
### 二叉树宽度
###二叉树非递归算法，使用栈    https://blog.yangx.site/2016/07/22/Python-binary-tree-traverse/
# # (1)#创建节点
# class Node(object):
#     def __init__(self,item):
#         self.item = item
#         self.lchirld = None
#         self.rchirld = None
#
# class Tree(object):
#     def __init__(self):
#         self.root = None
#     def add(self,item):
#         new_node = Node(item)
#         if self.root == None:
#             self.root = new_node
#         else:
#             queue = []
#             queue.append(self.root)
#             while queue:
#                 node = queue.pop(0)
#                 if node.lchirld == None:
#                     node.lchirld = new_node
#                     return
#                 if node.rchirld == None:
#                     node.rchirld = new_node
#                     return
#                 queue.append(node.lchirld)
#                 queue.append(node.rchirld)
#     #先序遍历
#     def preorder(self, root):
#         """递归实现先序遍历"""
#         if root:
#             print(root.item,end=' ')
#             self.preorder(root.lchirld)
#             self.preorder(root.rchirld)
#     #中序遍历
#     def inorder(self, root):
#         """递归实现中序遍历"""
#         if root:
#             self.inorder(root.lchirld)
#             print(root.item,end=' ')
#             self.inorder(root.rchirld)
#
#     def postorder(self, root):
#         """递归实现后续遍历"""
#         if root:
#             self.postorder(root.lchirld)
#             self.postorder(root.rchirld)
#             print(root.item,end=' ')
#
# tree = Tree()
# for i in range(10):
#     tree.add(i)
# #先序遍历
# tree.preorder(tree.root)
# print()
# #中序遍历
# tree.inorder(tree.root)
# print()
# #后序遍历
# tree.postorder(tree.root)

def frontStack(self, root):
    """利用堆栈前序遍历"""
    if root == None:
        return False
    stack = []
    node = root
    while node or stack:
        while node:  # 寻找左子树，压入栈内
            print(node.value, end=' ')
            stack.append(node)
            node = node.left
        node = stack.pop()
        node = node.right  # 开始寻找右子树


def midStack(self, root):
    """ 利用堆栈中序遍历"""
    if root == None:
        return False
    stack = []
    node = root
    while node or stack:
        while node:  # 从根结点开始，寻找左子树，把它压入栈中
            stack.append(node)
            node = node.left
        node = stack.pop()  # while 结束代表前一个节点没有了左子树
        print(node.value, end=' ')
        node = node.right  # 然后开始寻找右子树


def backStack(self, root):
    """利用堆栈后序遍历"""
    if root is None:
        return False
    stack1 = []
    stack2 = []
    stack1.append(root)
    while stack1:  # 找出后序遍历的逆序，存放在 stack2中
        node = stack1.pop()
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
        stack2.append(node)
    while stack2:  # 将 stack2中的元素出栈，即是后序遍历序列
        print(stack2.pop().value, end=' ')






# (2)
# class Node:
#      def __init__(self,value=None,left=None,right=None):
#          self.value=value
#          self.left=left    #左子树
#          self.right=right  #右子树
# def preTraverse(root):
#
#     '''
#      3     前序遍历
#      4     '''
#
#     if root == None:
#         return
#     print(root.value)
#     preTraverse(root.left)
#     preTraverse(root.right)
# def midTraverse(root):
#     '''
#          中序遍历
#     '''
#     if root == None:
#         return
#     midTraverse(root.left)
#     print(root.value)
#     midTraverse(root.right)
#
# def afterTraverse(root):
#
#     '''
#         后序遍历
#         '''
#     if root == None:
#         return
#     afterTraverse(root.left)
#     afterTraverse(root.right)
#     print(root.value)
# if __name__ == '__main__':
#
#     root = Node('D', Node('B', Node('A'), Node('C')), Node('E', right=Node('G', Node('F'))))
#
#     print('前序遍历：')
#
#     preTraverse(root)
#
#     print('\n')
#
#     print('中序遍历：')
#
#     midTraverse(root)
#
#     print('\n')
#
#     print('后序遍历：')
#
#     afterTraverse(root)
#
#     print('\n')
#


#
# #二叉树的三种遍历
# class Node():
#     def __init__(self,value=None,left=None,right=None):
#         self.value = value
#         self.left = left
#         self.right = right
# #
# # #先序遍历
# def preorder_traversal(root):
#     if root==None:
#         return
#     print(root.value)
#     preorder_traversal(root.left)
#     preorder_traversal(root.right)

# #中序遍历
# def inorder_traversal(root):
#     if root==None:
#         return
#     inorder_traversal(root.left)
#     print(root.value)
#     inorder_traversal(root.right)
#
# #后序遍历
# def postorder_traversal(root):
#     if root==None:
#         return
#     postorder_traversal(root.left)
#     postorder_traversal(root.right)
#     print(root)
#

"""广度优先遍历"""
# def breadth_travel(root):
#
#     if root is None:
#         return
#     else:
#         queue = []
#         queue.append(root)
#         print(len(queue))
#         while len(queue) > 0:
#             node = queue.pop(0)
#             print(node.value, end=" ")
#             print(len(queue))
#             if node.left:
#                 queue.append(node.left)
#                 print(len(queue))
#             if node.right:
#                 queue.append(node.right)
#                 print(len(queue))
#
#
# if __name__ == '__main__':
#     root = Node('a', Node('b', Node('c'), Node('d')), Node('e', Node('f'), Node('g')))
#     preorder_traversal(root)
#     breadth_travel(root)



#二叉树的三种遍历
# class Node():
#     def __init__(self,value,left=None,right=None,):
#         self.value = value
#         self.left = left
#         self.right = right
#     #前序遍历
# def pre_bianli(root):
#     if root ==None:
#         return
#     print(root.value)
#     pre_bianli(root.left)
#     pre_bianli(root.right)
# if __name__ == '__main__':
#     root = Node('4',Node('2',Node('1'),Node('3')),Node('7',Node('6'),Node('9')))
#     pre_bianli(root)


# class Node():
#     def __init__(self,value=None,left=None,right=None):
#         self.value = value
#         self.left = left
#         self.right = right
# def pre_tra(root):
#     if root==None:
#         return None
#     print(root.value)
#     pre_tra(root.left)
#     pre_tra(root.right)
#
# def ino_tra(root):
#     if root==None:
#         return
#     ino_tra(root.left)
#     print(root.value)
#     ino_tra(root.right)
#
# def pos_tra(root):
#     if root==None:
#         return
#     pos_tra(root.left)
#     pos_tra(root.right)
#     print(root.value)
#
#
# #广度优先遍历
# def guangdu(root):
#     if root==None:
#         return
#     queue = []
#     queue.append(root)
#     while len(queue)>0:
#         node = queue.pop(0)
#         print(node.value)
#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)
#
# #
# if __name__ == '__main__':
#     root = Node('a',Node('b',Node('c'),Node('d')),Node('e',Node('f'),Node('g')))
#     #root = Node('D', Node('B', Node('A'), Node('C')), Node('E', right=Node('G', Node('F'))))
#     #pre_tra(root)
#     ino_tra(root)
# #     pos_tra(root)
#     #guangdu(root)




class Node():
    def __init__(self,value=None,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

# #前序遍历
# def pre_bl(head):
#     if head==None:
#         return
#     print(head.value)
#     pre_bl(head.left)
#     pre_bl(head.right)
#
# #中序遍历
# def mid_bl(head):
#     if head==None:
#         return
#     pre_bl(head.left)
#     print(head.value)
#     pre_bl(head.right)
#
# #后序遍历
# def after_bl(head):
#     if head == None:
#         return
#     pre_bl(head.left)
#     pre_bl(head.right)
#     print(head.value)
#
# #层次遍历
# def cengci_bl(head):
#     if head == None:
#         return
#     queue = []
#     queue.append(head)
#     while len(queue)>0:
#         node = queue.pop(0)
#         print(node.value)
#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)
#
# if __name__ == '__main__':
#     #head = Node('a',Node('b',Node('c'),Node('d')),Node('e',Node('f'),Node('g')))
#     root = Node('a', Node('b', Node('c'), Node('d')), Node('e', Node('f'), Node('g')))
#     #pre_bl(head)
#     #mid_bl(head)
#     #after_bl(root)
#     cengci_bl(root)
#
#





def cengci(root):
    if root==None:
        return
    queue = []
    queue.append(root)
    while queue:
        node = queue.pop(0)
        print(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
if __name__ == '__main__':
    root = Node('a', Node('b', Node('c'), Node('d')), Node('e', Node('f'), Node('g')))
    cengci(root)