def minNumberInRotateArray(rotateArray):
    left = 0 #左侧的指针
    right = len(rotateArray) - 1 #右侧的指针
    mid = 0 #中间的指针
    if left==right:
        return rotateArray[left]
    while rotateArray[left] > rotateArray[right]:
        #当两个指针走到挨着的位置时，即right - left == 1,right就是最小数了
        if right - left == 1:
            mid = right
            break
        mid = left + (int)((right-left)/2)
        #若中间位置的数大于左边位置的数，说明最小的数在mid位置的右边中，让left走到mid的位置
        if rotateArray[mid] >= rotateArray[left]:
            left = mid
        #若中间位置的数小于右边指针位置的数，说明最小的数在mid位置的左边，让right走到mid的位置
        elif rotateArray[mid] < rotateArray[right]:
            right = mid
    return rotateArray[mid]

