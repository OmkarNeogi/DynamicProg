def firstMissingPositive(nums):
	nums.sort()
	if len(nums)<1:
		return 1
	result = -1
	for i in xrange(len(nums)):
		if nums[i] < 0:
			continue
		elif i>0 and nums[i-1]>0 and nums[i-1]+1 < nums[i]:
				result = nums[i-1]+1
		else:
			result = nums[0]+1
	return result

print(firstMissingPositive([2]))