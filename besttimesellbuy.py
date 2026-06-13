#best time to buy and stock brute force 
def besttime(nums):
    max=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            profit=nums[j]-nums[i]

            if profit > max:
                max=profit
    return max
nums=[5,1,3,7,4]
print(besttime(nums))

#.optimal solution
def bestsellbuy(nums):
    min_price= float('inf')
    max_profit=0

    for price in nums:
        if price < min_price:
            min_price=price
        if price-min_price > max_profit:
            max_profit=price-min_price
    return max_profit
nums=[5,1,3,7,4]
print(bestsellbuy(nums))