import random

def insertionSort(myList):
	n = len(myList)
	i=1
	while i<n:
		x = myList[i]
		j = i-1
		while (j>=0 and myList[j]>x):
			myList[j+1] = myList[j]
			j = j-1
		myList[j+1] = x
		i = i+1

	return myList


if __name__=="__main__":
	num_elements = random.randint(1,101)
	myList = random.sample(range(num_elements),num_elements);

	print("The un-sorted array is :")
	print(myList)
	myList = insertionSort(myList)
	print("The sorted array is :")
	print(myList)