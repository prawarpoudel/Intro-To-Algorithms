import random
def countingSort(myList,pos):	# pos gives the positinal info which we should sort by
	# the important consideration here is that the values in the array myList are
	# .. from 0 and some know highest value
	return_list = [0]*(len(myList)+1)
	counting_list = [0]*(10)

	for i in myList:
		# increase the index corresponding to value in myList
		counting_list[(i//pos)%10]+=1

	# print(counting_list)
	# find cumulative sum of  the array elements
	for i in range(1,len(counting_list)):
		counting_list[i] += counting_list[i-1]

	# print(counting_list)
	for i in myList[::-1]:
		return_list[counting_list[(i//pos)%10]] = i
		counting_list[(i//pos)%10] -= 1
	return return_list[1:]

def radixSort(myList,max_val):
	pos = 1
	while (max_val//pos)>0:
		myList = countingSort(myList,pos)
		pos *= 10
	return myList

if __name__=="__main__":
	num_elements = random.randint(0,101)
	max_val = num_elements-1
	myList = random.sample(range(max_val+1),num_elements);

	print("The un-sorted array is :")
	print(myList)
	myList = radixSort(myList,max_val)
	print("The sorted array is :")
	print(myList)