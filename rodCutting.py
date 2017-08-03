import sys

def rodCuting(price, length):
	opt = [-1]*length
	for i in xrange(length):
		x = price[i]
		for j in xrange(i):
			x = max(x, opt[j]+opt[i-1-j])
		opt[i] = x
	print(opt)
	return opt[length-1]

arr = [1,5,8,9,10,17,17,20]

print(rodCuting(arr, 8))