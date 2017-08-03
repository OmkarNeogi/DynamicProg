def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    l, r = 0, len(nums) - 1
        
    while l<r:
        middle = (l+r)/2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            l = middle
        elif nums[middle] > target:
            r = middle - 1
    return len(nums)
print(searchInsert([1,3,4], 2))