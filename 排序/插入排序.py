# def insertionSort(arr):
#     for i in range(len(arr)):
#         preIndex = i - 1
#         current = arr[i]
#         while preIndex >= 0 and arr[preIndex] > current:
#             arr[preIndex + 1] = arr[preIndex]
#             preIndex -= 1
#         arr[preIndex + 1] = current
#     return arr
# c
# insertionSort(arr)
# print(arr)

# 将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后
# 一个元素当成是未排序序列。
#
# 从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。
# （如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）











#重复练习
# def insert_sort(arr):
#     for i in range(len(arr)):
#         preindex = i-1
#         current = arr[i]
#         while preindex>=0 and arr[preindex]>current:
#             arr[preindex+1] = arr[preindex]
#             preindex -= 1
#         arr[preindex+1] = current
#     return arr
# arr = [1,3,2]
# i = insert_sort(arr)
# print(i)



#插入排序

# def insert_sort(arr):
#     for i in range(len(arr)):
#         preindex = i-1
#         current = arr[i]
#         while preindex>=0 and arr[preindex]>current:
#             arr[preindex+1]=arr[preindex]
#             preindex-=1
#         arr[preindex+1]=current
#     return arr
# arr=[1,4,3,2]
# print(insert_sort(arr))






# def insert_sort(arr):
#     for i in range(len(arr)):
#         perindex = i-1
#         current = arr[i]
#         while perindex>=0 and arr[perindex]>current:
#           arr[perindex+1]=arr[perindex]
#           perindex-=1
#         arr[perindex+1]=current
#     return arr
#
# arr=[1,4,3,2]
# print(insert_sort(arr))
#























# def insert_sort(arr):
#     for i in range(len(arr)):
#         preindex = i-1
#         current = arr[i]
#         while preindex>=0 and arr[preindex]>current:
#             arr[preindex+1]=arr[preindex]
#             preindex -=1
#         arr[preindex+1]=current
#
#     return arr
# arr = [4,3,1,2]
# #arr = [1,2,5,4,6,8,9,7]
# print(insert_sort(arr))
#
#
#
#
#
#
#
#
#
def insert_sort(arr):
    for i in range(len(arr)):
        cur = arr[i]
        pre = i-1
        while pre>=0 and arr[pre]>cur:
            arr[pre+1] = arr[pre]
            pre -=1
        arr[pre+1]=cur
    return arr


arr = [1,2,5,4,6,8,9,7]
print(insert_sort(arr))


































