#Given a sorted array and a target element, count how many times 
#the target appears in the array.

def countOccurrences(nums, target):
    low1= 0
    high1= len(nums) - 1
    first= -1
    while low1 <= high1:
        mid1 = (low1 + high1) // 2

        if nums[mid1] == target:
            first = mid1
            high1 = mid1 - 1

        elif nums[mid1] < target:
            low1 = mid1 + 1

        else:
            high1 = mid1 - 1

    low2 = 0
    high2 = len(nums) - 1
    last = -1
    while low2 <= high2:
        mid2 = (low2 + high2) // 2

        if nums[mid2] == target:
            last = mid2
            low2 = mid2 + 1

        elif nums[mid2] < target:
            low2 = mid2 + 1

        else:
            high2 = mid2 - 1

    return (last - first) + 1


nums = [2,3,5,5,5,5,7,9]
target = 5

print(countOccurrences(nums, target))