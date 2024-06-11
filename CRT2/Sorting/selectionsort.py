#selection sort
def performselectionSort(nums):
    n=len(nums)
    pos=n-1
    while pos > 0:
        maxEleIndex=pos
        for i in range(0,pos-1):
            if nums[maxEleIndex] < nums[i]:
                maxEleIndex=i 
        if maxEleIndex != pos:
            temp=nums[maxEleIndex]
            nums[maxEleIndex]=nums[pos]
            nums[pos]=temp        
        pos -= 1

nums=[9,8,7,6,5,4,3,2,1]
print("Before sorting:",nums)
performselectionSort(nums)
print("After sorting:" , nums) 