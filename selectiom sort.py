#Selection sort
def performSelectionSort(nums):
    n=len(nums)
    fixThisPosition=n-1
    while fixThisPosition>0:
        maxEleIndex=fixThisPosition
        for index in range(0,fixThisPosition-1):
            if nums[maxEleIndex]<nums[index]:
                maxEleIndex=index
            if maxEleIndex!=fixThisPosition:
                temp=nums[maxEleIndex]
                nums[maxEleIndex]=nums[fixThisPosition]
                nums[fixThisPosition]=temp
            fixThisPosition -= 1
nums=[9.3,8,4,6,5,0,1,2,7]
print("Before Sorting:",nums)
performSelectionSort(nums)
print("After Sorting:",nums)