import random

def fixNodeForHeap(myList,idx):
	'''
	This function creates a heap at a node idx and its subtree
	'''
	n = len(myList)-1
	# left child at 2*idx+1
	if 2*idx+1 <= n:
		# means left child exists for node at idx
		temp = 2*idx+1
		if 2*idx+2 <= n:
			# means right child also exists
			# ..now get the largest child
			if myList[2*idx+2]>myList[2*idx+1]:
				temp = 2*idx+2

		if myList[idx] < myList[temp]:
			tVal = myList[temp]
			myList[temp] = myList[idx]
			myList[idx] = tVal
			myList = fixNodeForHeap(myList,temp)
	return myList

def makeHeap(myList,idx =  0):
	n = len(myList)-1
	if(2*idx+1 <= n):
		myList = makeHeap(myList,2*idx+1)
	if(2*idx+2 <= n):
		myList = makeHeap(myList,2*idx+2)
	myList = fixNodeForHeap(myList,idx)
	return myList

def heapSort(myList):
	myList = makeHeap(myList)
	for i in range(len(myList)-1,0,-1):
		temp = myList[i]
		myList[i] = myList[0]
		myList[0] = temp
		myList[:i] = fixNodeForHeap(myList[:i],0)
	return myList

if __name__=="__main__":
	num_elements = random.randint(0,101)
	max_val = num_elements-1
	myList = random.sample(range(max_val+1),num_elements);

	print("The un-sorted array is :")
	print(myList)
	myList = heapSort(myList)
	print("The sorted array is :")
	print(myList)