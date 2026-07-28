#Height Checker solution using Bubble Sort
class Solution:
    def heightChecker(self, heights):
        expected = heights[:]
        n = len(expected)

        for i in range(n):
            swapped = False
            for j in range(n - i - 1):
                if expected[j] > expected[j + 1]:
                    expected[j], expected[j + 1] = expected[j + 1], expected[j]
                    swapped = True

            if not swapped:
                break

        count = 0
        for i in range(n):
            if heights[i] != expected[i]:
                count += 1

        return count

heights = list(map(int, input("Enter the heights: ").split()))

obj = Solution()
result = obj.heightChecker(heights)

print("Number of students in wrong positions:", result)