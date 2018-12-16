import random

def merge(left_list,right_list):
	lleft = len(left_list)
	lright = len(right_list)

	return_list = [None]*(lleft+lright)
	lidx = 0
	ridx = 0
	idx = 0
	while idx<(lleft+lright):
		if lidx>=lleft:
			# integration from left array is completed
			return_list[idx] = right_list[ridx]
			ridx += 1
		elif ridx>=lright:
			# similar to above
			return_list[idx] = left_list[lidx]
			lidx += 1
		else:
			if left_list[lidx]<=right_list[ridx]:
				return_list[idx] = left_list[lidx]
				lidx += 1
			else:
				return_list[idx] = right_list[ridx]
				ridx += 1
		idx += 1
	return return_list

a = [2,3,6]
b = [1,4,5,8]
print(merge(a,b))