# Problem: 278. First Bad Version
# Link: https://leetcode.com/problems/first-bad-version/description/
# Difficulty: Easy
def firstBadVersion(self, n):
        low, high = 0, n
        while low < high:
            mid = (low + high) //2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low
