#binary search to find the first bad version,
bad = 4   # Assume version 4 is the first bad version

def isBadVersion(version):
    return version >= bad

def firstBadVersion(n):
    low = 1
    high = n
    ans = -1

    while low <= high:
        mid = low + (high - low) // 2

        if isBadVersion(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


print(firstBadVersion(5))