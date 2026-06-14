#Finding majority element from the list
'''def majority(nums):
    freq={}
    for num in nums:
        freq[num]=freq.get(num,0)+1
    max_element=max(freq,key=freq.get)
    if max_element > len(nums)//2:
        return max_element
    else:
        return "majority does not exist"
nums=[3,2,3,1,2,4]
print(majority(nums))'''

def majorityelement(nums):
    seen=None
    count=0
    for num in nums:
        if count==0:
            seen=num
        if num==seen:
            count+=1
        else:
            count-=1
    return seen
nums=[3,2,3]
print(majorityelement(nums))
    

