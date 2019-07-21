##递归  还可以用循环加yeild
import time
def Fibonacci_Recursion_tool(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci_Recursion_tool(n - 1) + Fibonacci_Recursion_tool(n - 2)

def Fibonacci_Recursion(n):
    result_list = []
    for i in range(1, n + 1):
        result_list.append(Fibonacci_Recursion_tool(i))
    return result_list
strat = time.time()
f = Fibonacci_Recursion(30)
print(f)
end = time.time()
print(end-strat)