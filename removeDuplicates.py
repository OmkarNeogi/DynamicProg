def removeDuplicates(nums):
    i = 0
    for j in range(1, len(nums)):
        if(nums[j] != nums[i]):
            i += 1
            nums[i] = nums[j]
    print(nums)
    return i + 1

def remElement(nums, val):
    i=0
    for j in range(len(nums)-1, -1, -1):
        if(nums[j] == val):
            del nums[j]
        else:
            i += 1
    print(nums)
    print('length '+str(i))

def removeElement(nums, val):
    i = 0
    for j in range(0, len(nums)):
        if(nums[j] == val):
            continue
        if(nums[i] == val):
            del nums[i]
            i -= 1
        i += 1
    print(str(i))
    print(nums)
print(remElement([1,2,3,4],1))
