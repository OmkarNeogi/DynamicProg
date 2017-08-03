nums = [-2,0,0,2,2]

def threeSum(nums):
    nums.sort()
    result = []
    
    if(len(nums) == 0):
        return []

    if(nums[0]>0 or nums[len(nums)-1]<0):
        return []

    zero_index = -1
    for i in range(len(nums)):
        if i>0 and nums[i] >= 0 and nums[i-1] < 0:
            zero_index = i
            break
    left_sum  = abs(sum(nums[0:zero_index]))
    right_sum = sum(nums[zero_index:])
    while(nums[len(nums)-1] > left_sum):
        del nums[-1]
    while(nums[0] > right_sum):
        del nums[0]

    for i in xrange(len(nums)-2):
        if i>0 and nums[i] == nums[i-1]:
            continue

        l = i+1
        r = len(nums) - 1

        while(l<r):
            s = nums[i] + nums[l] + nums[r]

            if   s<0:
                l += 1
            elif s>0:
                r -= 1
            else:
                result.append((nums[i], nums[l], nums[r]))
                while l<r and nums[l] == nums[l+1]:
                    l += 1
                while l<r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
    return result

print(threeSum(nums))