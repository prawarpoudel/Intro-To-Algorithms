# This is the simple search code for GIT repo.

# This is random library
import random	
def simple_search(myList,key):
	'''
	This function takes a list and an element.
	If the element is in the list, it returns the Index of the item in list
		else it returns -1
	'''
	n=len(myList)
	for i in range(n):
		if myList[i]==key:
			return i
	return -1

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
	index_returned =simple_search(myList,key_to_search)	#our answer is already in index_returned

	print("Found {} at index {} in array {}".format(key_to_search,index_returned,myList))

	# folllwing does the checking
	if verify(myList,index_returned,key_to_search)==True:
		print("The algorithm works correctly")
	else:
		print("Algo Not working")