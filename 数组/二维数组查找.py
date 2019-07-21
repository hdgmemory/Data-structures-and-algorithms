def find(array,num):
    row = 0
    col = len(array[0])-1
    if array == None:
        return False
    while row<len(array) and col >=0:
        if array[row][col] == num:
            return True
        elif array[row][col] > num:
            col -=1
        else:
            row +=1
    return False

m = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
print(find(m,2))




#剑指offer
# https://kaiyuanyokii2n.com/offer-python.html