#最基础的四个算法：冒泡、选择、插入、快排中，快排的时间复杂度最小O(n*log2n)，其他都是O（n2）
#最基础的四个算法：冒泡、选择、插入、快排中，快排的时间复杂度最小O(n*log2n)，其他都是O（n2）
#冒泡排序、插入排序是稳定的
#选择排序、快速排序是不稳定的




# def QuickSort(myList,start,end):
#     #判断low是否小于high,如果为false,直接返回
#     if start < end:
#         i,j = start,end
#         #设置基准数
#         base = myList[i]
#         while i < j:
#             #如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
#             while (i < j) and (myList[j] >= base):
#                 j = j - 1
#             # 6  1  2 7  9  3  4  5 10  8  j=9
#             #  5   1  2 7  9  3  4  6  10  8  j=7
#             #  5  1  2 6  9  3  4  7  10  8   i=3
#             #  5  1  2 4  9  3  6  7  10  8   j=6
#             #  5  1  2 4  6  3  9  7  10  8   i=4
#             #  5  1  2 4  3  6  9  7  10  8
#             # 5 1 2 4 3 j=4
#             # 1 2 3 4 5
#             #如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
#             myList[i],myList[j] = myList[j], myList[i]
#             #同样的方式比较前半区
#             while (i < j) and (myList[i] <= base):
#                 i = i + 1
#             myList[j],myList[i] = myList[i],myList[j]
#         #做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
#         # myList[i] = base
#
#         #递归前后半区
#         QuickSort(myList, start, i - 1)
#         QuickSort(myList, j + 1, end)
#     return myList
#
#
# myList = [6  ,1 , 2 ,7  ,9 , 3  ,4 , 5 ,10, 56, 8,19]
# print("Quick Sort: ")
# QuickSort(myList,0,len(myList)-1)
# print(myList)

# http://www.cnblogs.com/ahalei/p/3568434.html
# 1）设置两个变量i、j，排序开始的时候：i = 0，j = N - 1；
# 2）以第一个数组元素作为关键数据，赋值给key，即key = A[0]；
# 3）从j开始向前搜索，即由后开始向前搜索(j - -)，找到第一个小于key的值A[j]，将A[j]
# 和A[i]
# 互换；
# 4）从i开始向后搜索，即由前开始向后搜索(i + +)，找到第一个大于key的A[i]，将A[i]
# 和A[j]
# 互换；
# 5）重复第3、4
# 步，直到i = j； (3, 4
# 步中，没找到符合条件的值，即3中A[j]
# 不小于key, 4
# 中A[i]
# 不大于key的时候改变j、i的值，使得j = j - 1，i = i + 1，直至找到为止。找到符合条件的值，进行交换的时候i， j指针位置不变。另外，i == j这一过程一定正好是i + 或j - 完成的时候，此时令循环结束）。
#
#
#
# 时间复杂度：O(nlgn)

#重复练习

# def query_sort(start,end,arr):
#     if start < end :
#         i,j = start,end
#         base = arr[i]
#         while i<j:
#             while (i<j) and (arr[j]>=base):
#                 j=j-1
#             arr[i],arr[j]=arr[j],arr[i]
#             while (i<j) and (arr[i]<=base):
#                 i=i+1
#             arr[j], arr[i] = arr[i], arr[j]
#         arr[i]=base
#         query_sort(start,i-1,arr)
#         query_sort(j+1,end,arr)
#     return arr
#
# arr = [1,3,9,8,6,7,4,5,10]
# print(arr)
# query_sort(0,len(arr)-1,arr)
# print(arr)

# def quike_sort(arr,start,end):
#     if start<end:
#
#
# #重复练习(1)
# def query_sort(arr,statrt,end):
#     if statrt<end:
#         i,j = statrt,end
#         base = arr[i]
#         while i<j:
#             while i<j and arr[j]>= base:
#                 j -= 1
#             arr[i],arr[j] = arr[j],arr[i]
#             while i<j and arr[i] <= base:
#                 i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#         # arr[i] = base
#         query_sort(arr,statrt,i-1)
#         query_sort(arr,i+1,end)
#         return arr
#
# arr = [1,4,5,5,8,7,9,2,3]
# b = query_sort(arr,0,len(arr)-1)
# print(b)

#重复练习（2）
# def quick_sort(arr,start,end):
#     if start < end:
#         i = start
#         j = end
#         base = arr[i]
#         while i < j:
#             while i < j and arr[j] >= base:
#                 j -= 1
#             arr[j],arr[i] = arr[i],arr[j]
#
#             while i < j and arr[i] <= base:
#                 i += 1
#             arr[i], arr[j]= arr[j], arr[i]
#         arr[i] = base
#         quick_sort(arr,start,i-1)
#         quick_sort(arr,i+1,end)
#     return arr
# arr = [1,2,5,3,9,4]
# qk = quick_sort(arr,0,len(arr)-1)
# print(qk)



#重复练习（3）
# def quick_sort(start,end,arr):
#     if start<end:
#         i, j = start,end
#         base = arr[i]
#         while i<j:
#             while i<j and arr[j]>base:
#                 j-=1
#             arr[j],base=base,arr[j]
#             while i<j and arr[i]<base:
#                 i+=1
#             arr[i],base=base,arr[i]
#         quick_sort(start,i-1,arr)
#         quick_sort(i+1,end,arr)
#     return arr
# arr = [1,3,2,8,7,9,4,6,5]
# print(quick_sort(0,len(arr)-1,arr))



#快排
# def quick_sort(start,end,arr):
#     if start<end:
#         i,j=start,end
#         base = arr[i]
#         while i<j:
#             while i<j and arr[j]>=base:
#                 j-=1
#             arr[j],arr[i]=arr[i],arr[j]
#             while i<j and arr[i]<=base:
#                 i+=1
#             arr[i],arr[j]=arr[j],arr[i]
#         quick_sort(start,i-1,arr)
#         quick_sort(i+1,end,arr)
#     return arr
# arr=[1,4,3,2,7,6,9]
# print(quick_sort(0,len(arr)-1,arr))
#













def qucik_sort(arr,start,end):
    if start < end:
        i,j = start,end
        base = arr[i]
        if i<j:
            while i<j and arr[j]>=base:
                j-=1
            arr[i],arr[j]=arr[j],arr[i]
            while i<j and arr[i]<=base:
                i+=1

            arr[i],arr[j]=arr[j],arr[i]
        arr[i] = base
        qucik_sort(arr,start,i-1)
        qucik_sort(arr,i+1,end)
        return arr
if __name__ == '__main__':
        arr = [1, 4, 3, 2, 7, 6, 9]
        print(qucik_sort(arr,0,len(arr)-1))







