# Linear Search 
 
nums = [12, 34, 21, 23, 44, 56];
target = 23 
position = -1
for index in range(len(nums)):
    if nums[index] == target:
        position = index 
        break 
 
if position == -1:
    print("Target not found")
else:
    print("Target found at position: ", position)