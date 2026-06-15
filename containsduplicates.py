#Contains duplicates
def containsduplicates(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                return True
    return False
nums=[1,2,3,]
print(containsduplicates(nums))

def containsdup(nums):
    nums.sort()
    for i in range(1,len(nums)):
        if nums[i-1]==nums[i]:
            return True
        
    return False
nums=[1,2,3,1,2]
print(containsdup(nums))