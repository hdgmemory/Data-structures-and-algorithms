# 前提是列表有序
# 返回 x 在 arr 中的索引，如果不存在返回 -1
#复杂度Ο(logn)
def binarySearch(arr, l, r, x):
    # 基本判断
    if r >= l:
        #一定加int，防止列表为偶数
        mid = int((l + r )/ 2)

        # 元素整好的中间位置
        if arr[mid] == x:
            return mid

            # 元素小于中间位置的元素，只需要再比较左边的元素
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

            # 元素大于中间位置的元素，只需要再比较右边的元素
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # 不存在
        return -1


# 测试数组
arr = [2, 3, 4, 10, 40]
x = 10

# 函数调用
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("元素在数组中的索引为 %d" % result)
else:
    print("元素不在数组中")


##找峰值
def findPeakElement(nums):

    left = 0
    right = len(nums) - 1
    while left <= right:
        if left == right:
            return nums[left]

        mid = int((left + right)/2)
        # 如果中间小于右边，那么一定在右边
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        # 左边不小于右边，那么直接把右边弄到中间
        else:
            # right不可以是mid-1，万一正好是mid，就跳过了，因为并没有比对mid的值
            right = mid

nums = [1,2,3,5,4,3,2,1,6,4,3,2,1]
f = findPeakElement(nums)
print(f)
