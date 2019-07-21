#设置指针交换
arr=[1,2,3,4,5,6,7,8]
def tzarr(arr):
    strat = 0
    end = len(arr)-1
    while strat <= end:
        if arr[strat]%2==0:
            if arr[end]%2==1:
                arr[strat],arr[end]=arr[end],arr[strat]
            end -= 1
            continue
        strat += 1

    return arr
t = tzarr(arr)
print(t)