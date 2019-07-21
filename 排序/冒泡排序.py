# arr = [1,3,6,8,9,4,5,2,32]
# def bubbleSort(arr):
#     for i in range(1,len(arr)):
#         for j in range(0,len(arr)-i):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     return arr
# bubbleSort(arr)
# print(arr)



# 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
#
# 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
#
# 针对所有的元素重复以上的步骤，除了最后一个。
#
# 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

# https://www.cnblogs.com/wuxinyan/p/8615127.html

# #重复练习
#arr = [1,3,6,8,9,4,5,2,32]
# arr = [4,3,1,2]
# def bubble_sort(arr):
#     for i in range(len(arr)-1):
#         for j in range(1,len(arr)-i):
#             if arr[j]>arr[j-1]:
#                 arr[j],arr[j-1]=arr[j-1],arr[j]
#     return arr
# bubble_sort(arr)
# print(arr)






#冒泡排序
# arr = [1,4,3,2]
# def bubble_sort(arr):
#     for i in range(1,len(arr)):
#         for j in range(len(arr)-i):
#             if arr[j]>arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
# b = bubble_sort(arr)
# print(b)















#冒泡排序
# def bubble_sort(arr):
#     for i in range(len(arr)-1):
#         for j in range(1,len(arr)-i):
#             if arr[j-1]>arr[j]:
#                 arr[j-1],arr[j]=arr[j],arr[j-1]
#     return arr
# arr = [1,3,2,9,8,7,5,6]
# print(bubble_sort(arr))






# def bubble_sort(arr):
#     for i in range(len(arr)-1):
#         for j in range(1,len(arr)-i):
#             if arr[j-1]>arr[j]:
#                 arr[j-1],arr[j]=arr[j],arr[j-1]
#     return arr
# arr = [1,4,3,2,6,5]
# print(bubble_sort(arr))
#


# def bubble_sort(arr):
#     for i in range(len(arr)-1):
#         for j in range(1,len(arr)-i):
#             if arr[j-1]>arr[j]:
#                 arr[j-1],arr[j]=arr[j],arr[j-1]
#     return arr
# #arr = [4,3,1,2]
# arr = [1,3,6,8,9,4,5,2,32]
# b = bubble_sort(arr)
# print(b)
#
#



# def bubble_sort(arr):
#     for i in range(len(arr)-1):
#         for j in range(1,len(arr)-i):
#             if arr[j-1]>arr[j]:
#                 arr[j-1],arr[j]=arr[j],arr[j-1]
#     return arr
#
# arr = [1,3,6,8,9,4,5,2,32]
# b = bubble_sort(arr)
# print(b)
#
#



def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(1,len(arr)-i):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]

    return arr
arr = [1,3,6,8,9,4,5,2,32]
b = bubble_sort(arr)
print(b)







