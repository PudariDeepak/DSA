'''def maximumsubarray(nums):
    max=float("-inf")
    for i in range(len(nums)):
        sum=0
        for j in range(i,len(nums)):
            sum+=nums[j]
            if sum>max:
                max=sum
    return max
nums=[2,-8,7,2]
print(maximumsubarray(nums))'''


#optimal solution
def maximumSubArray(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

nums = [2, -8, 7, 2]
print(maximumSubArray(nums))
