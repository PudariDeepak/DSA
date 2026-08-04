#Writing a python code for the bubble sort
arr=[7,4,2,9,8,1]

for i in range(0,len(arr)):
    min=i
    for j in range(i+1,len(arr)):
        if arr[j] < arr[min]:
            min = j
    arr[min],arr[i] = arr[i],arr[min]
print(arr)
