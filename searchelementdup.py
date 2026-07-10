#You are given the rotated sorted array nums (which may contain duplicates) 
#and a target integer. You must return true if the target exists in nums, 
#or false if it does not
def nums(arr,target):
    low=0
    high=len(arr)-1
    while(low <= high):
        mid=(low+high)//2
        if arr[mid]==target:
            return True
        if(arr[low]==arr[mid] and arr[mid]==arr[high]):
            low+=1
            high-=1
        elif(arr[low] <= arr[mid]):
            if (target>= arr[low] and target<arr[mid]):
                high=mid-1
            else:
                low=mid+1
        else:
            if (target>arr[mid] and target<=arr[high]):
                low=mid+1
            else:
                high=mid-1
    return False
arr=[2,5,6,0,0,1,2]  
target=2
print(nums(arr,target))