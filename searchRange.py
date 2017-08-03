def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    def search(n):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) / 2
            if nums[mid] >= n:
                hi = mid
            else:
                lo = mid + 1
        return lo
    
    lo = search(target)
    print(search(target+1))
    return [lo, search(target+1)-1] if target in nums[lo:lo+1] else [-1, -1]

print(searchRange([1,2,2,2], 2))