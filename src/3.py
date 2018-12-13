import random

def selectionSort(myList):
	n = len(myList)

	for i in range(n-1):
		c_index = i
		for j in range(i+1,n):
			if myList[j]<myList[c_index]:
				c_index = j
		
		# swap the item in c_index and i
		temp = myList[c_index]
		myList[c_index] = myList[i]
		myList[i] = temp

	return myList


if __name__=="__main__":
	num_elements = random.randint(1,101)
	myList = random.sample(range(num_elements),num_elements);

	print("The un-sorted array is :")
	print(myList)
	myList = selectionSort(myList)
	print("The sorted array is :")
	print(myList)