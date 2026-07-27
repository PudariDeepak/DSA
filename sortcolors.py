class Solution:
    def sortColors(self, nums):
        n = len(nums)

        for i in range(n):
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return nums


nums = list(map(int, input("Enter the array elements (0, 1, 2): ").split()))

obj = Solution()
result = obj.sortColors(nums)

print("Sorted Colors:", result)