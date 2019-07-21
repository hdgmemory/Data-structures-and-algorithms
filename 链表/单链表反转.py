#单链表中插入和删除遵循"先连后断"

# 建立三个变量，L、M、R互相赋值迭代，并建立指向关系，从而实现单链表的反转。
class Node():
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def func(head):
    if head == None:
        return head
    L,M,R = None,None,head
    while R.next != None:
        L = M
        M = R
        R = R.next
        M.next = L
    R.next = M
    return R
if __name__ == '__main__':
    l1 = Node(1)
    l1.next =Node(2)
    l1.next.next = Node(3)
    l1.next.next.next = Node(4)
    l = func(l1)
    print(l.data,l.next.data,l.next.next.data,l.next.next.next.data)




# class Node():
#     def __init__(self,data,next=None):
#         self.data = data
#         self.next = next
#
# def func(head):
#     if head==None:
#         return head
#     a,b,c,d = None,None,None,head
#     while d.next !=None:
#         a = b
#         b = c
#         c = d
#         d = d.next
#         c.next = a
#     c.next = b
#     d.next = c
#     return d
#
#
# if __name__ == '__main__':
#     l1 = Node(1)
#     l1.next =Node(2)
#     l1.next.next = Node(3)
#     l1.next.next.next = Node(4)
#     l = func(l1)
#     print(l.data,l.next.data,l.next.next.data,l1.next.next.next.data)
#




#
#
#
#
#
#
#

#
#
# class Node():
#     def __init__(self,data,next=None):
#         self.data = data
#         self.next = next
#
# def func(jd):
#     if jd==None:
#         return
#     M,L,R = None,None,jd
#     while R.next!=None:
#         M=L
#         L=R
#         R=R.next
#         L.next=M
#     R.next=L
#     return R
# if __name__ == '__main__':
#     l1 = Node(1)
#     l1.next = Node(2)
#     l1.next.next = Node(3)
#     l = func(l1)
#     print(l.data,l.next.data,l.next.next.data)











# class Node():
#     def __init__(self,data=None,next=None):
#         self.data = data
#         self.next = next
# def reverse(head):
#     if head==None:
#         return
#     l,m,r=None,None,head
#     while r.next!=None:
#         l=m
#         m=r
#         r=r.next
#         m.next=l
#     r.next=m
#     return r
# l = Node('1')
# l.next = Node('2')
# l.next.next = Node('3')
# l1 = reverse(l)
# print(l1.data,l1.next.data,l1.next.next.data)




# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# def ReverseList(pHead):
#     if not pHead:
#         return None
#     # 当前节点是pHead，Pre为当前节点的前一节点，Next为当前节点的下一节点
#     # 需要pre和next的目的是让当前节点从pre->head->next1->next2变成pre<-head next1->next2
#     # 即pre让节点可以反转所指方向，但反转之后如果不用next节点保存next1节点的话，此单链表就此断开了
#     # 所以需要用到pre和next两个节点
#     # 1->2->3->4->5
#     # 1<-2<-3 4->5
#     Pre = None
#     Next = None
#     while pHead:
#         Next = pHead.next # 保存当前结点的next指针，方便反转第一次后，在链表断开的情况下，依然找到原来的下一个结点
#         pHead.next = Pre # 反转链表，将当前结点的next指针指向前一个结点
#          让pre，pHead依次向后移动一个节点，继续下一次的指针反转
#         Pre = pHead
#         pHead = Next
#     return Pre
#
# if __name__ == '__main__':
#     l1 = Node(1)
#     l1.next =Node(2)
#     l1.next.next = Node(3)
#     l1.next.next.next = Node(4)
#     l = ReverseList(l1)
#     print(l.data,l.next.data,l.next.next.data,l.next.next.next.data)


###输入一个链表，从尾到头打印链表每个节点的值
# class Node():
#     def __init__(self,data=None,next=None):
#         self.data = data
#         self.next = next
#
# def bianli(data):
#     l = []
#     if data==None:
#         return
#     while data:
#         l.append(data)
#         data = data.next
#     return l[::-1]
#
# if __name__ == '__main__':
#     l1 = Node(1)
#     l1.next = Node(2)
#     l1.next.next = Node(3)
#     b = bianli(l1)
#     for i in b:
#         print(i.data)

###链表中倒数第k个结点
###思路：个人总结最佳算法，先计算链表的长度，然后计算找到倒数第k个需要几次循环，
# 并判断其中关系。最后用for循环，不断将指针指向下一个节点，即为所求。
# class Node():
#     def __init__(self,data=None,next=None):
#         self.data = data
#         self.next = next
#
# def find_node(data,k):
#     len_node = 0
#     temp = data
#     while temp:
#         temp = temp.next
#         len_node += 1
#     if k<0 and len_node-k<0:
#         return
#     for i in range(len_node-k):
#         data = data.next
#     return data
#
# if __name__ == '__main__':
#     l1 = Node(1)
#     l1.next = Node(2)
#     l1.next.next = Node(3)
#     b = find_node(l1,2)
#     print(b.data)


# class Node():
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# def recurse(head, newhead):  # 递归，head为原链表的头结点，newhead为反转后链表的头结点
#     if head is None:
#         return
#     if head.next is None:
#         newhead = head
#     else:
#         newhead = recurse(head.next, newhead)
#         head.next.next = head
#         head.next = None
#     return newhead
#
# if __name__ == '__main__':
#     l1 = Node(1)
#     l1.next = Node(2)
#     l1.next.next = Node(3)
#     b = recurse(l1,None)
#     print(b.val,b.next.val,b.next.next.val)
# ###合并两个排序的链表
##https://blog.csdn.net/wstcjf/article/details/78064842

class Node():
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

def fanzhuan(head):
    if head==None:
        return
    a,b,c = None,None,head
    while head.next!=None:
        a = b
        b = c
        c = c.next
        b.next = a
    c.next = b
    return c
# if __name__ == '__main__':
#     l1 = Node(1)
#     l1.next = Node(2)
#     l1.next.next = Node(3)
#     l1.next.next.next = Node(4)
#     l = fanzhuan(l1)
#     print(l.value,l.next.value,l.next.next.value,l.next.next.next.value)


if __name__ == '__main__':
    l1 = Node(1)
    l1.next =Node(2)
    l1.next.next = Node(3)
    l1.next.next.next = Node(4)
    l = fanzhuan(l1)
    print(l.value,l.next.value,l.next.next.value,l.next.next.next.value)






























