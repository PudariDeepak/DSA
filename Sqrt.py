#Given a non-negative integer x, return the square root of x 
#rounded down to the nearest integer. The returned integer must 
# also be non-negative.
def squareroot(x):
    low=0
    high=x
    ans=-1
    while(low <= high):
        mid=(low+high)//2
        if (mid*mid <= x):
            ans=mid
            low = mid+1
        else:
            high = mid-1
    return ans
x=int(input("Enter a non-negative integer: "))
print(squareroot(x))