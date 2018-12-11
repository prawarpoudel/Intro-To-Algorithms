# This is the simple search code for GIT repo.

# This is random library
import random	
import math
def binary_search(myList,key):
	'''
	Iterative:
	This function takes a list and an element.
	If the element is in the list, it returns the Index of the item in list
		else it returns -1
	'''
	right = len(myList)-1
	left = 0

	index = -1
	while(left<=right):
		mid = math.floor((right+left)/2)
		if(key<myList[mid]):
			right = mid-1
		elif(key>myList[mid]):
			left = mid+1
		else:
			index = mid
			break
	return index

def verify(myList,index,key):
	'''
	This function verifies the operation of searching is correct
	'''
	if index<0:
		return "Not Found in Array"
	if myList[index]==key:
		return True
	else:
		return False

if __name__=="__main__":
	num_elements = random.randint(1,101)
	myList = random.sample(range(num_elements),num_elements);

	key_to_search = random.randint(0,num_elements-1)
	myList.sort()
	index_returned =binary_search(myList,key_to_search)	#our answer is already in index_returned

	print("Found {} at index {} in array {}".format(key_to_search,index_returned,myList))

	# folllwing does the checking
	if verify(myList,index_returned,key_to_search)==True:
		print("The algorithm works correctly")
	else:
		print("Algo Not working")