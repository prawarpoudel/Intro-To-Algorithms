import random
import math
import sys

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

def mergeSort(myList):
	n = len(myList)
	if(n>1):
		mid = (n//2)
		left_list = myList[0:mid]
		right_list = myList[mid:n]

		left_list = mergeSort(left_list)
		right_list = mergeSort(right_list)

		myList = merge(left_list,right_list)
	return myList

if __name__=="__main__":
	num_elements = random.randint(1,101)
	myList = random.sample(range(num_elements),num_elements);

	print("The un-sorted array is :")
	print(myList)
	myList = mergeSort(myList)
	print("The sorted array is :")
	print(myList)