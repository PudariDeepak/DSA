#two arrys sorting
'''def arraysort(nums1,nums2,m,n):
    for i in range(0,n):
        nums1[m+i]=nums2[i]
    nums1.sort()
    return nums1
nums1=[1,2,3,0,0,0]
nums2=[2,4,5]
m=3
n=3
print(arraysort(nums1,nums2,m,n))'''


def twoarraysort(nums1,nums2,m,n):
    i=0
    j=0
    res=[]
    while (i<m and j<n):
        if nums1[i]<nums2[j]:
            res.append(nums1[i])
            i+=1
        else:
            res.append(nums2[j])
            j+=1
    while i<m:
        res.append(nums1[i])
        i+=1
    while j<n:
        res.append(nums2[j])
        j+=1
    for k in range(0,m+n):
        nums1[k]=res[k]
    return nums1
nums1=[1,2,3,0,0,0]
nums2=[2,5,6]
m=3
n=3
print(twoarraysort(nums1,nums2,m,n))

#Two sum
'''def twosum(nums,target):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return i,j
nums=[2,7,11,15]
target=9
print(twosum(nums,target))


def twosums(nums,target):
    res={}
    for i in range(len(nums)):
        
        x=target-nums[i]
        if x  in res:
           return res[x],i
        
        res[nums[i]]=i
nums=[2,7,11,15]
target=26
print(twosums(nums,target))'''