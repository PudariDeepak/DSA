##removing duplicates from the sorted list and returning no.of elements in the non-duplicates list
def removingdup(nums):
    non_duplicates=[]
    for i in range(len(nums)):
        if nums[i] not in non_duplicates:
            non_duplicates.append(nums[i])
    return len(non_duplicates)
nums=[1,1,2,2,2,3,3,4]
print(removingdup(nums))


#optimal solution
def removedup(nums):
    i=0
    j=1
    while j<=len(nums)-1:
        if nums[i] != nums[j]:
            nums[i+1]=nums[j]
            i+=1
        j+=1
    return i+1
nums=[1,1,2,2,2,3,3,4]
print(removedup(nums))