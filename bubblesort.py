#Writing a python code for the bubble sort
arr = [4,3,2,7,8,5,6,1]
n = len(arr)
for i in range(n-2,-1,-1):
    for j in range(0,i+1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr)