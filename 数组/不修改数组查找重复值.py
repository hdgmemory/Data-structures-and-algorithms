class Solution(object):
    def findDuplicate(self,numbers):
        def countRange(head, tail):
            count = 0
            for ele in numbers:
                if ele >= head and ele <= tail:
                    count += 1
            return count

        if not numbers:
            return -1
        n = len(numbers)
        start = 1
        end = n-1
        while end >= start:
            middle = (end - start)//2 + start
            ct = countRange(start, middle)
            if end == start:
                if ct > 1:
                    return start
                else:
                    break

            if ct > (middle - start +1):
                end = middle
            else:
                start = middle +1
        return -1


##利用辅助空间的话，时间和空间复杂度都是O(n)；利用下标于数字对应关系的话时间复杂度是O(n)
# 空间复杂度是O(l),但是需要改变数组；利用二分查找类似思路的方法，时间复杂度是O(nlogn)
# 空间复杂度O(l)