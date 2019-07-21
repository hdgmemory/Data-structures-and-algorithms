
# 申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；
#
# 设定两个指针，最初位置分别为两个已经排序序列的起始位置；
#
# 比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；
#
# 重复步骤 3 直到某一指针达到序列尾；
#
# 将另一序列剩下的所有元素直接复制到合并序列尾。
import math
arr = [12,8,5,7,6,1,4,3,2,9]
def mergeSort(arr):
    if (len(arr) < 2):
        return arr
    middle = math.floor(len(arr) / 2)
    left, right = arr[0:middle], arr[middle:]
    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

a = mergeSort(arr)
print(a)