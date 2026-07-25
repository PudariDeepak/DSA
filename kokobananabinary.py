#Binary search problem on koko eating bananas nd return how many bananas 
# eat at particular given time per hour
def speed(n,piles):
    total = 0
    for i in piles:
        total += (i+n-1) // n
    return total
def minEatingspeed(piles,h):
    low = 1
    high = max(piles)
    ans = -1
    while (low <= high):
        mid = (low + high ) //2
        if(speed(mid,piles) <= h):
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return  ans
piles=[30,11,23,4,20]
h=7
print(minEatingspeed(piles,h))