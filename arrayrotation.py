#shifting of 1st element inthe array to the last position-leftshifting
'''def rotate(arr):
    temp=arr[0]
    for i in range(1,len(arr)):
        arr[i-1]=arr[i] 
    arr[-1]=temp
    return arr
arr=[1,2,3,4,5]
print(rotate(arr))'''

#shifting of last element inthe array to the first position-rightshifting
def rotate(arr):
    temp=arr[-1]
    for i in range(len(arr)-2,-1,-1):
        arr[i+1]=arr[i]
    arr[0]=temp
    return arr
arr=[1,2,3,4,5]
print(rotate(arr))