# arr = [1,4,3,2]
# def selectionSort(a):
#     for i in range(0,len(a)-1):
#         minIndex = i
#         for j in range(i+1,len(a)):
#             if a[minIndex]>a[j]:
#                 minIndex = j
#         if i!=minIndex:
#             a[i],a[minIndex]=a[minIndex],a[i]
#     return a
# selectionSort(arr)
# print(arr)

# 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
#
# 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
#
# 重复第二步，直到所有元素均排序完毕。


# 重复练习
# arr = [1,6,5,8,7,9,2,3,12]
# def selection_sort(arr):
#     for i in range(len(arr)-1):
#         min = i
#         for j in range(i+1,len(arr)):
#             if arr[j]<arr[min]:
#                 min = j
#         if  min != i :
#             arr[i],arr[min] = arr[min],arr[i]
#     return arr
# a = selection_sort(arr)
# print(a)
#






# #重复练习
# arr = [1,6,5,8,7,9,2,3,12]
# def selection_sort(arr):
#     for i in range(len(arr)-1):
#         min=i
#         for j in range(i+1,len(arr)-1):
#             if arr[j]<arr[min]:
#                 min=j
#         if i!=min:
#             arr[i],arr[min]=arr[min],arr[i]
#     return arr
# s = selection_sort(arr)
# print(s)
















# 重复练习（1）
# arr = [1,3,2,6,5,8,7,4,9]
# def selection_sort(arr):
#     for i in range(len(arr)-1):
#         min = i
#         for j in range(i+1,len(arr)-1):
#             if arr[j]<arr[min]:
#                 min = j
#         if i != min:
#             arr[i],arr[min] = arr[min],arr[i]
#     return arr
# print(selection_sort(arr))





#重复练习（2）
# def select_sort(arr):
#     for i in range(len(arr)-1):
#         min = i
#         for j in range(i+1,len(arr)-1):
#             if arr[j]<arr[min]:
#                 min = j
#         if min!=i:
#             arr[i],arr[min]=arr[min],arr[i]
#     return arr
# arr = [1,4,3,2]
# print(select_sort(arr))




















#选择排序
arr = [1,6,5,8,7,9,2,3,12]
def select_sort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min = j
        if min!=i:
            arr[min],arr[i]=arr[i],arr[min]
    return arr
print(select_sort(arr))



