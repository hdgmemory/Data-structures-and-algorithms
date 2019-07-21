# 哈希表思想    数组无序
def getRes_HashMap(nums, target):
    result = []
    for i, value in enumerate(nums):
        if (target - value) in nums[i+1:]:
            result.append((value, target - value))
    return result




# 快速排序思想    数组有序
def getRes_QuickSort(nums, target):
    nums = sorted(nums)
    len1 = len(nums)
    res = []
    if len1>= 2:
        low, high = 0, len1-1
        while low < high:
            if nums[low] + nums[high] == target:
                res.append((nums[low], nums[high]))
                low += 1
                high -= 1
            elif nums[low] + nums[high] > target:
                high -= 1
            else:
                low += 1
        return res
