def firstandlastindex(nums,target):
    low1=0
    high1=len(nums)-1
    ans1=-1
    while(low1<=high1):
        mid=(low1+high1)//2
        if nums[mid]==target:
            ans1=mid
            high1=mid-1
        elif target<nums[mid]:
            high1=mid-1
        else:
            low1=mid+1
    low2=0
    high2=len(nums)-1
    ans2=-1
    while(low2<=high2):
        mid=(low2+high2)//2
        if nums[mid]==target:
            ans2=mid
            low2=mid+1
        elif target<nums[mid]:
            high2=mid-1
        else:
            low2=mid+1
    return ans1,ans2
nums=[1,2,3,4,5,6,6,6,6,6,6,6,7]
target=6
print(firstandlastindex(nums,target))
        
    
