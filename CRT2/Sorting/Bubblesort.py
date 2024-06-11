#Bubble Sort
def performBubbleSort(nums):
    n=len(nums)
    pos=n-1
    while pos > 0:
        for i in range(0,pos):
            if nums[i] >  nums[i+1]:
                nums[i] , nums[i+1] = nums[i+1],nums[i]
        print(nums)
        pos -= 1
nums=[9,8,7,6,5,4,3,2,1]
print("Before sorting:",nums)
performBubbleSort(nums)
print("After sorting:" , nums)                