# class Solution():
#     # matrix类型为二维列表，需要返回列表
#     def printMatrix(self,matrix):
#         res = []
#         while matrix:
#             res += matrix.pop(0)
#             if matrix and matrix[0]:
#                 for row in matrix:
#                     res.append(row.pop())
#             if matrix:
#                 res += matrix.pop()[::-1]
#             if matrix and matrix[0]:
#                 for row in matrix[::-1]:
#                     res.append(row.pop(0))
#         return res
#
# matrix=[[123],[4,5,6]]
# s = Solution()
# print(s.printMatrix(matrix))