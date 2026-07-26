def hours_required(speed, piles):
    total_hours = 0
    for pile in piles:
        total_hours += (pile + speed - 1) // speed   # Ceiling division
    return total_hours

def minEatingSpeed(piles, h):
    max_speed = max(piles)
    # Try every possible eating speed
    for speed in range(1, max_speed + 1):
        if hours_required(speed, piles) <= h:
            return speed

    return -1

# Driver Code
piles = [3, 6, 7, 11]
h = 5
print(minEatingSpeed(piles, h))