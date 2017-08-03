def search(nums, target):
    length = len(nums)
    if length == 0:
        return -1
    
    last_element = nums[length - 1]

    if last_element == target:
        return length - 1
    
    i = 0
    for i in xrange(len(nums)-1, -1, -1):
        if nums[i] == target:
            return i
        if nums[i] > last_element:
            break

    for j in xrange(i + 1):
        if(nums[j] == target):
            return j

print(search([5,6,7,0,1,2,4], 6))