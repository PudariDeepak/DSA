#Relative Sort Array solution using Bubble Sort
class Solution:
    def relativeSortArray(self, arr1, arr2):
        # Bubble Sort arr1
        n = len(arr1)
        for i in range(n):
            for j in range(n - i - 1):
                if arr1[j] > arr1[j + 1]:
                    arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j]

        result = []

        for num in arr2:
            while num in arr1:
                result.append(num)
                arr1.remove(num)

        result.extend(arr1)

        return result


arr1 = list(map(int, input("Enter arr1 elements: ").split()))
arr2 = list(map(int, input("Enter arr2 elements: ").split()))

obj = Solution()
result = obj.relativeSortArray(arr1, arr2)

print("Relative Sorted Array:", result)