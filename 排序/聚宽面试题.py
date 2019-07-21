
# # （2）找到并删除当前目录下的.pyc文件
# #windows
# import os
# del_paths = [name for name in os.listdir('.') if name.endswith('.pyc')]
# for del_path in del_paths:
#     os.remove(del_path)
# #linux
# #find . -name '*.pyc' | xagrs rm -rf



#（3）查找最长连续子字符串，输入str='abbbbcccddddddddeee'    输出'dddddddd'
import time
str='abbbbcccdddddddda'
def longest_repetition(chars):
    if len(chars) == 0 or len(chars) == 1:
        return (chars,len(chars))
    result = [1]*len(chars)
    for left in range(len(chars)-1):
        for right in range(left+1, len(chars)):
            if chars[right-1] == chars[right]:
               result[left] += 1
            else:
                break
    print(result)
    return (chars[result.index(max(result))]*max(result))

print(longest_repetition(str))







