import random
def quick_sort_help(myList,left,right):
	# take the left most or the first element as pivot,
	#.. so we compare from the elements left+1 to right
	l_idx = left+1
	r_idx = right

	while(l_idx<=r_idx):
		if(myList[l_idx]<=myList[left]):
			# if the element is less or equal, we are fine with it
			l_idx += 1
		elif(myList[r_idx]>=myList[left]):
			r_idx -= 1
		else:
			temp = myList[l_idx]
			myList[l_idx] = myList[r_idx]
			myList[r_idx] = temp
			l_idx += 1
			r_idx -= 1
	temp = myList[left]
	myList[left] = myList[r_idx]
	myList[r_idx] = temp

	return myList,r_idx

def quickSort(myList,left,right):
	if(left<right):
		myList,pivot = quick_sort_help(myList,left,right)
		quickSort(myList,left,pivot-1)
		quickSort(myList,pivot+1,right)

	return myList

if __name__=="__main__":
	num_elements = random.randint(1,101)
	myList = random.sample(range(num_elements),num_elements);

	print("The un-sorted array is :")
	print(myList)
	myList = quickSort(myList,0,num_elements-1)
	print("The sorted array is :")
	print(myList)