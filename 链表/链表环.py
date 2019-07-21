# 第一步，找环中相汇点。分别用p1，p2指向链表头部，p1每次走一步，p2每次走二步，直到p1==p2找到在环中的相汇点。
#
# 第二步，找环的入口。接上步，当p1==p2时，p2所经过节点数为2x,p1所经过节点数为x,设环中有n个节点,\
# p2比p1多走一圈有2x=n+x; n=x;可以看出p1实际走了一个环的步数，再让p2指向链表头部，p1位置不变，p1,p2
# 每次走一步直到p1==p2;此时p1指向环的入口。 



# class Node():  # 定义一个Node类，构造两个属性，一个是item节点值，一个是节点的下一个指向
#     def __init__(self, item=None):
#         self.item = item
#         self.next = None

# def findbeginofloop(head):  # 判断是否为环结构并且查找环结构的入口节点
#     slowPtr = head  # 将头节点赋予slowPtr
#     fastPtr = head  # 将头节点赋予fastPtr
#     loopExist = False  # 默认环不存在，为False
#     if head == None:  # 如果头节点就是空的，那肯定就不存在环结构
#         return False
#     while fastPtr.next != None and fastPtr.next.next != None:  # fastPtr的下一个节点和下下个节点都不为空
#         slowPtr = slowPtr.next  # slowPtr每次移动一个节点
#         fastPtr = fastPtr.next.next  # fastPtr每次移动两个节点
#         if slowPtr == fastPtr:  # 当fastPtr和slowPtr的节点相同时，也就是两个指针相遇了
#             loopExist = True
#             print("存在环结构")
#             break
#     if loopExist == True:
#         slowPtr = head
#         while slowPtr != fastPtr:
#             fastPtr = fastPtr.next
#             slowPtr = slowPtr.next
#         return slowPtr
#
#     print("不是环结构")
#     return False
#
#
# if __name__ == "__main__":
#      node1 = Node(1)
#      node2 = Node(2)
#      node3 = Node(3)
#      node4 = Node(4)
#      node5 = Node(5)
#      node1.next = node2
#      node2.next = node3
#      node3.next = node4
#      node4.next = node5
#      node5.next = node2
#      print(findbeginofloop(node1).item)


# # 重复练习
#
# class Node():
#     def __init__(self,data,next=None):
#         self.data = data
#         self.next = next
# def find_loop(head):
#     fastPtr = head
#     slowPtr = head
#     loopExit = False
#     if head == None:
#         return None
#     while (head.next!=None and head.next.next!=None):
#         fastPtr = fastPtr.next.next
#         slowPtr = slowPtr.next
#         if fastPtr==slowPtr:
#             print('存在环结构')
#             loopExit = True
#             break
#     if loopExit == True:
#         # slowPtr = head
#         fastPtr = head
#         while slowPtr!=fastPtr:
#             fastPtr = fastPtr.next
#             slowPtr = slowPtr.next
#         return slowPtr
#     print('不存在环')
#     return False
# if __name__ == '__main__':
#     node1 =  Node(1)
#     node2 =  Node(2)
#     node3 =  Node(3)
#     node4 =  Node(4)
#     node5 =  Node(5)
#     node1.next = node2
#     node2.next = node3
#     node3.next = node4
#     node4.next = node5
#     node5.next = node2
#     print(find_loop(node1).data)


# # 重复练习
# class Node():
#     def __init__(self,data,next=None):
#         self.data = data
#         self.next = next
#
# def loop_lb(head):
#     fastnode = head
#     slownode = head
#     loopExit = False
#     if head==None:
#         return None
#     while slownode.next!=None and fastnode.next.next!=None:
#         slownode = slownode.next
#         fastnode = fastnode.next.next
#         if slownode==fastnode:
#             print('存在环结构')
#
#             loopExit = True
#             break
#     if loopExit==True:
#         slownode = head
#         while slownode!=fastnode:
#             slownode = slownode.next
#             fastnode = fastnode.next
#         return slownode
#     print('不存在环')
#     return False
# if __name__ == '__main__':
#     node1 = Node(1)
#     node2 = Node(2)
#     node3 = Node(3)
#     node4 = Node(4)
#     node5 = Node(5)
#     node6 = Node(6)
#     node1.next = node2
#     node2.next = node3
#     node3.next = node4
#     node4.next = node5
#     node5.next = node6
#     node6.next = node4
#     print(loop_lb(node1).data)
#
#
#
# class Node():
#     def __init__(self,data=None,next=None):
#         self.data = data
#         self.next = next
# def loop(head):
#     fastnode = head
#     slownode = head
#     loopexit = False
#     if head==None:
#         return None
#     #while slownode.next != None and fastnode.next.next != None:
#     while fastnode.next.next!=None and slownode.next!=None:
#
#         fastnode = fastnode.next.next
#         slownode = slownode.next
#         if fastnode==slownode:
#             print('存在环')
#             loopexit = True
#             break
#
#     if loopexit==True:
#         fastnode = head
#         while slownode!=fastnode:
#
#             fastnode = fastnode.next
#             slownode = slownode.next
#         return fastnode
#     print('不存在环')
#     return False
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node5 = Node(5)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# node5.next = node4
# print(loop(node1).data)














class Node():
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

def loop_lb(value):
    fast_loop = value
    slow_loop = value
    loopexit = False
    if value == None:
        return None
    while slow_loop.next!=None and fast_loop.next.next!=None:
        fast_loop = fast_loop.next.next
        slow_loop = slow_loop.next
        if fast_loop==slow_loop:
            print('存在环')
            loopexit = True
            break

    if loopexit == True:
        slow_loop=value
        while slow_loop!=fast_loop:
            slow_loop=slow_loop.next
            fast_loop = fast_loop.next
        return slow_loop
    print('不存在环')
    return False

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node3
    print(loop_lb(node1).value)



