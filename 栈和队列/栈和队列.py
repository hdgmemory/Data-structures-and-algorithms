# https://www.cnblogs.com/hwf-73/p/7705100.html
#两个队列实现栈
# class StackWithTwoQueues(object):
#      def __init__(self):
#          self._stack1 = []
#          self._stack2 = []
#
#      def push(self,x):
#          if len(self._stack1) == 0:
#              self._stack1.append(x)
#          elif len(self._stack2) == 0:
#              self._stack2.append(x)
#          if len(self._stack2) == 1 and len(self._stack1) >= 1:
#              while self._stack1:
#                  self._stack2.append(self._stack1.pop(0))
#          elif len(self._stack1) == 1 and len(self._stack2) > 1:
#              while self._stack2:
#                  #self._stack1.insert(0,self._stack2.pop(0))
#                  self._stack1.append(self._stack2.pop(0))
#
#      def pop(self):
#          if self._stack1:
#              return self._stack1.pop(0)
#          elif self._stack2:
#              return self._stack2.pop(0)
#          else:
#               return None

# class stack_with_twoqueues():
#     def __init__(self):
#         self.queue1 = []
#         self.queue2 = []
#     def push(self,x):
#         if len(self.queue1)==0:
#             self.queue1.append(x)
#         elif len(self.queue2)==0:
#             self.queue2.append(x)
#         if len(self.queue2)==1 and len(self.queue1)>=1:
#             while self.queue1:
#                 self.queue2.append(self.queue1.pop(0))
#         elif len(self.queue1)==1 and len(self.queue2)>1:
#             while self.queue2:
#                 self.queue1.append(self.queue2.pop(0))
#     def pop(self):
#         if self.queue1:
#            return self.queue1.pop(0)
#         elif self.queue2:
#            return self.queue2.pop(0)
#         else:
#             return  None
#
# if __name__ == '__main__':
#     s = stack_with_twoqueues()
#     s.push('1')
#     s.push('2')
#     s.push('3')
#     s.push('4')
#     s.push('5')
#     s.push('6')
#     print(s.pop())
#     print(s.pop())
#     print(s.pop())
#     print(s.pop())
#     print(s.pop())
#     print(s.pop())

# ## 重复练习
# class zhan():
#     def __init__(self):
#         self.stack1=[]
#         self.stack2=[]
#
#     def push(self,x):
#         if len(self.stack1)==0:
#             self.stack1.append(x)
#         elif len(self.stack2)==0:
#             self.stack2.append(x)
#         if len(self.stack1)==1 and len(self.stack2)>=1:
#             while self.stack2:
#                 self.stack1.append(self.stack2.pop(0))
#         elif len(self.stack2)==1 and len(self.stack1)>1:
#             while self.stack1:
#                 self.stack2.append(self.stack1.pop())
#     def pop(self):
#         if self.stack1:
#             return self.stack1.pop(0)
#         elif self.stack2:
#             return self.stack2.pop(0)
#         else:
#             return None
# if __name__ == '__main__':
#     z = zhan()
#     z.push('1')
#     z.push('2')
#     z.push('3')
#     print(z.pop())
#     print(z.pop())
#     print(z.pop())









###########两个栈实现队列
# class QueueWithTwoStacks(object):
#      def __init__(self):
#          self._stack1 = []
#          self._stack2 = []
#
#      def appendTail(self,x):
#          self._stack1.append(x)
#
#      def deleteHead(self):
#           if self._stack2:
#               return self._stack2.pop()
#           else:
#               if self._stack1:
#                  while self._stack1:
#                      self._stack2.append(self._stack1.pop())
#                  return self._stack2.pop()
#               else:
#                   return None
#
# if __name__ == '__main__':
#      z = QueueWithTwoStacks()
#      z.appendTail('1')
#      z.appendTail('2')
#      z.appendTail('3')
#      print(z.deleteHead())
#      print(z.deleteHead())
#      print(z.deleteHead())






# class queue_with_twostacks():
#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []
#     def append(self,x):
#         self.stack1.append(x)
#     def delete(self):
#         if self.stack2:
#             return self.stack2.pop()
#         else:
#             if self.stack1:
#                 while self.stack1:
#                     self.stack2.append(self.stack1.pop())
#                     return self.stack2.pop()
#             else:
#                 return None
# s = queue_with_twostacks()
# s.append('1')
# s.append('2')
# s.append('3')
# print(s.delete())
# print(s.delete())
# print(s.delete())


















# class StactWithQueues():
#     def __init__(self):
#         self.start1 = []
#         self.start2 = []
#     def push(self,x):
#         if len(self.start1)==0:
#             self.start1.append(x)
#         elif len(self.start2)==0:
#             self.start2.append(x)
#         if len(self.start2)==1 and len(self.start1)>=1:
#             while self.start1:
#                 self.start2.append(self.start1.pop(0))
#         elif len(self.start1)==1 and len(self.start2)>1:
#             while self.start2:
#                 self.start1.append(self.start2.pop(0))
#
#     def pop(self):
#         if self.start1:
#             self.start1.pop(0)
#         elif self.start2:
#             self.start2.pop(0)
#         else:
#             return None




# 用两个栈实现队列，实现入队和出队方法
# class Queue(object):
#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []
#     #入队
#     def enqueue(self,element):
#         if self.stack1:
#             self.stack1.append(element)
#         else:
#             while self.stack2:
#                 self.stack1.append(self.stack2.pop())
#             self.stack1.append(element)
#     #出队
#     def dequeue (self):
#         if self.stack2:
#             return self.stack2.pop()
#         elif self.stack1:
#             while self.stack1:
#                 self.stack2.append(self.stack1.pop())
#             return self.stack2.pop()
#         else:
#             return None
#
# if __name__=='__main__':
#     queue = Queue()
#     queue.enqueue('1')
#     queue.enqueue('2')
#     queue.enqueue('3')
#     queue.enqueue('4')
#     print (queue.dequeue())
#     print (queue.dequeue())
#     print (queue.dequeue())
#     print (queue.dequeue())
#
#   入队时，先判断s1是否为空，如不为空，说明所有元素都在s1，此时将入队元素直接压入s1；如为空，
#  要将s2的元素逐个“倒回”s1，再压入入队元素。
#   出队时，先判断s2是否为空，如不为空，直接弹出s2的顶元素并出队；如为空，将s1的元素逐个“倒入”
# s2，把最后一个元素弹出并出队。

# 重复练习
# class Queue():
#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []
#     # 入队
#     def enqueue(self,x):
#         if self.stack1:
#             self.stack1.append(x)
#         else:
#             if self.stack2:
#                 while self.stack2:
#                     self.stack1.append(self.stack2.pop())
#             self.stack1.append(x)
#     # 出队
#     def dequeue(self):
#         if self.stack2:
#             return self.stack2.pop()
#         elif self.stack1:
#             while self.stack1:
#                 self.stack2.append(self.stack1.pop())
#             return self.stack2.pop()
#         else:
#             return None
#
# if __name__=='__main__':
#     queue = Queue()
#     queue.enqueue('1')
#     queue.enqueue('2')
#     queue.enqueue('3')
#     queue.enqueue('4')
#     print (queue.dequeue())
#     print (queue.dequeue())
#     print (queue.dequeue())
#     print (queue.dequeue())




# class duilie():
#     def __init__(self):
#         self.stack1=[]
#         self.stack2=['4']
#     #入队
#     def enter_queue(self,x):
#         if self.stack1:
#             self.stack1.append(x)
#         else:
#             while self.stack2:
#                 self.stack1.append(self.stack2.pop())
#             self.stack1.append(x)
#     #出队
#     def out_queue(self):
#         if self.stack1:
#             while self.stack1:
#                 self.stack2.append(self.stack1.pop())
#             return self.stack2.pop()
#         elif self.stack2:
#             return self.stack2.pop()
#         else:
#             return None
#
# if __name__ == '__main__':
#     d = duilie()
#     d.enter_queue('1')
#     d.enter_queue('2')
#     d.enter_queue('3')
#     print(d.out_queue())
#     print(d.out_queue())
#     print(d.out_queue())






#两个队列实现栈
# class stack_twoqueue():
#     def __init__(self):
#         self.queue1 = []
#         self.queue2 = []
#
#     def push(self,x):
#         if len(self.queue1)==0:
#             self.queue1.append(x)
#         elif len(self.queue2)==0:
#             self.queue2.append(x)
#         if len(self.queue2)==1 and len(self.queue1)>0:
#             while self.queue1:
#                 self.queue2.append(self.queue1.pop(0))
#         elif len(self.queue1)==1 and len(self.queue2)>0:
#             while self.queue2:
#                 self.queue1.append(self.queue2.pop(0))
#
#     def pop(self):
#         if self.queue1:
#             return self.queue1
#         elif self.queue2:
#             return self.queue2
#         else:
#             return None
# if __name__ == '__main__':
#     s = stack_twoqueue()
#     s.push(1)
#     s.push(2)
#     s.push(3)
#     s.push(4)
#     s.push(5)
#     print(s.pop())
#     # print(s.pop())
#     # print(s.pop())
#     # print(s.pop())
#     # print(s.pop())
#
#


# #两个栈实现队列
# class queue_twostack():
#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []
#
#     def inqueue(self,x):
#         self.stack1.append(x)
#         # if self.stack1:
#         #     self.stack1.append(x)
#         # else:
#         #     if self.stack2:
#         #         while self.stack2:
#         #             self.stack1.append(self.stack2.pop())
#         #     self.stack1.append(x)
#     def outqueue(self):
#         if self.stack1:
#             while self.stack1:
#                 self.stack2.append(self.stack1.pop())
#             return self.stack2.pop()
#         elif self.stack2:
#             return self.stack2.pop()
#         else:
#             return None
#
# if __name__ == '__main__':
#     q = queue_twostack()
#     q.inqueue(1)
#     q.inqueue(2)
#     q.inqueue(3)
#     q.inqueue(4)
#     print(q.outqueue())
#     print(q.outqueue())
#     print(q.outqueue())
#     print(q.outqueue())




#两个栈实现队列
# class twostack_queue():
#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []
#
#     def push(self,x):
#         self.stack1.append(x)
#
#     def pop(self):
#         if self.stack1:
#             while self.stack1:
#                 self.stack2.append(self.stack1.pop())
#             return self.stack2.pop()
#         elif self.stack2:
#             return self.stack2.pop()
#         else:
#             return
#
# if __name__ == '__main__':
#     s = twostack_queue()
#     s.push(1)
#     s.push(2)
#     s.push(3)
#     s.push(4)
#     s.push(5)
#     print(s.pop())
#     print(s.pop())
#     print(s.pop())
#     print(s.pop())
#     print(s.pop())
#




class twoqueue_stack():
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self,x):
        if len(self.queue1)==0:
            self.queue1.append(x)
        elif len(self.queue2)==0:
            self.queue2.append(x)
        if len(self.queue2)==1 and len(self.queue1)>=1:
            while self.queue1:

                self.queue2.append(self.queue1.pop(0))
        elif len(self.queue1)==1 and len(self.queue2)>=1:
            while self.queue2:
                self.queue1.append(self.queue2.pop(0))

    def pop(self):
        if self.queue1:
            return self.queue1.pop(0)
        else:
            return self.queue2.pop(0)


if __name__ == '__main__':
    s = twoqueue_stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
