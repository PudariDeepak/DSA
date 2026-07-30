class Solution:
    def sortedSquares(self, nums):
        squares = []
        for num in nums:
            squares.append(num * num)

        n = len(squares)
        for i in range(n):
            swapped = False
            for j in range(n - i - 1):
                if squares[j] > squares[j + 1]:
                    squares[j], squares[j + 1] = squares[j + 1], squares[j]
                    swapped = True

            if not swapped:
                break

        return squares

nums = list(map(int, input("Enter the sorted array: ").split()))

obj = Solution()
result = obj.sortedSquares(nums)

print("Sorted Squares:", result)