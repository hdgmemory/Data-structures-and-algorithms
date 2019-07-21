class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

    # def __del__(self):
    #     self.val = None
    #     self.next = None

class Solution():
    def DeleteNode(self, pListHead, pToBeDeleted):
        if not pListHead or not pToBeDeleted:
            return None

        if pToBeDeleted.next != None:
            temp = pToBeDeleted.next
            pToBeDeleted.val = temp.val
            pToBeDeleted.next = temp.next
            del temp
        elif pListHead == pToBeDeleted:
            del pListHead
            del pToBeDeleted
        else:
            temp = pListHead
            while temp.next != pToBeDeleted:
                temp = temp.next
            temp.next = None
            del pToBeDeleted

if __name__ == '__main__':
    # l1 = Node(1)
    # l1.next =Node(2)
    # l1.next.next = Node(3)
    # l1.next.next.next = Node(4)

    # s = Solution()
    # s.DeleteNode(l1,l1)
    # print(l1.val,l1.next.val,l1.next.next.val)