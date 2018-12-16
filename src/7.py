import random
def countingSort(myList,max_val):
	# the important consideration here is that the values in the array myList are
	# .. from 0 and some know highest value
	return_list = [0]*(len(myList)+1)
	counting_list = [0]*max_val

	for i in myList:
		# increase the index corresponding to value in myList
		counting_list[i]+=1

	# print(counting_list)
	# find cumulative sum of  the array elements
	for i in range(1,len(counting_list)):
		counting_list[i] += counting_list[i-1]

	# print(counting_list)
	for i in myList[::-1]:
		return_list[counting_list[i]] = i
		counting_list[i] -= 1
	return return_list[1:]

if __name__=="__main__":
	num_elements = random.randint(0,101)
	myList = random.sample(range(num_elements),num_elements);

	print("The un-sorted array is :")
	print(myList)
	myList = countingSort(myList,num_elements)
	print("The sorted array is :")
	print(myList)