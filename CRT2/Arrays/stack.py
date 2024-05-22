#implementing stacks using arrays
def push(stack, ele):
    stack.insert(0, ele)
    print(ele, " inserted into stack successfully")
 
def pop(stack):
    if len(stack) == 0:
        print("stack is empty")
        return 
    print(stack[0], "deleted successfully")
    stack.pop(0)
 
stack = []
push(stack, 10)
push(stack, 20)
push(stack, 30)
push(stack, 40)
push(stack, 50)
 
print(stack)
 
pop(stack)
print(stack)
 
pop(stack)
print(stack)
 
pop(stack)
print(stack)
 
pop(stack)
print(stack)
 
pop(stack)
print(stack)
 
pop(stack)
 
 
 
 
 
 
 
 
# Output
# 10  inserted into stack successfully
# 20  inserted into stack successfully
# 30  inserted into stack successfully
# 40  inserted into stack successfully
# 50  inserted into stack successfully
# [50, 40, 30, 20, 10]
# 50 deleted successfully
# [40, 30, 20, 10]
# 40 deleted successfully
# [30, 20, 10]
# 30 deleted successfully
# [20, 10]
# 20 deleted successfully
# [10]
# 10 deleted successfully
# []
# stack is empty
# []
 
 
 
 
 
 
 
 
 
 
print(stack)
