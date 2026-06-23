'''def movingzeros(nums):
    res=[]
    res_zero=[]
    for num in nums:
        if num != 0:
            res.append(num)
        else:
            res_zero.append(num)
    return res+res_zero

nums=[1,0,3,0,0,4,5]
print(movingzeros(nums))'''

#optimal solution with inplace
def movingzeroes(nums):
   pos=0
   for i in range(0,len(nums)):
        if nums[i] != 0:
            temp=nums[i]
            nums[i]=nums[pos]
            nums[pos]=temp
            pos+=1
   return nums
nums=[0,0,1,0,4,0,8,0]
print(movingzeroes(nums))
        
           
    

      