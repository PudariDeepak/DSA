#Given an array of integers, return all the leaders in the array.
def leaders(arr):
    result = []
    max_right = float('-inf')

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] >= max_right:
            result.append(arr[i])
            max_right = arr[i]

    return result[::-1]


arr = [16, 17, 4, 3, 5, 2]
print(leaders(arr))