def threeSumClosest(nums, target):

	nums.sort()
	
	prev = 9223372036854775807
	result = None

	for i in xrange(len(nums)-2):
		l = i + 1
		r = len(nums) - 1
		while l<r:
			s = nums[i] + nums[l] + nums[r]

			if s == target:
				return s
			elif s < target:
				l += 1
				# print('gone right: %d,%d,%d'%(i,l,r))
			elif s > target:
				r -= 1
				# print('gone left: %d,%d,%d'%(i,l,r))
			if abs(target-s) < prev:
				result = s
				prev = abs(target - s)
		# print('new round')

	return result
print(threeSumClosest([0,0,0], 12))