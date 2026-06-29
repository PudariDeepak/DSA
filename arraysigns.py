# Rearrage the array  with signs
'''def signs(nums):
   pos=[]
   neg=[]
   for i in range(len(nums)):
        if nums[i]>0:
            pos.append(nums[i])
        else:
            neg.append(nums[i])
   k=0
   for j in range(0,len(pos)):
        nums[k]=pos[j]
        nums[k+1]=neg[j]
        k+=2
   return nums
nums=[3,-1,4,-5,-2,6]
print(signs(nums))'''  

def signs(nums):
    n=len(nums)
    pos=0
    neg=1
    res=[0]*n
    for i in range(len(nums)):
        if nums[i]>0:
            res[pos]=(nums[i])
            pos+=2
        else:
            res[neg]=(nums[i])
            neg+=2
    return res
nums=[3,1,-2,-5,4,-1]
print(signs(nums))
    