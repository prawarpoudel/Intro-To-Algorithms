# Description:  
This repository contains the software implementations of all the algorithms that I, as a student, studied while my time at UAH for undergraduate course "Intro to Design and Analysis of Algorithms". I have presented here more practical side of the course. By this I mean, I have presented implementations of the studied algorithms rather than the acutal theoritical explanations of the concepts. Although, I have to admit that I might as well present some theoritical explanations as well.

I might add some extra coding practises that are helpful at the end, after the section **Project2** ends. Lets see how far I can go with that.

A discretion advise to all is that this is not supposed to be a single stop for solution to assignments for others, but is intended to serve as a referral place for myself. The materials presented here, although, are hand-typed by me, do (may) not belong to me.

***

## The Start:  
  
Any algorithm course starts with the theoritical definitions of Growth of Functions. There are basically six-ways of expressing the growth of functions (as I have been taught as of now). Bit-O, Bit-θ, and Bit-Ω and the lowercase versions of each of them. There are a lot of materials online that explains these concepts in detail. Please refer to one of them if you are some one who is not me. For myself, I would refer to [this line for quick refresher](https://cathyatseneca.gitbooks.io/data-structures-and-algorithms/content/analysis/notations.html) and [this link for another refresher](https://stackoverflow.com/questions/1364444/difference-between-big-o-and-little-o-notation).

One important thing to keep in mind as a student is the following sequencee. While analyzing algorithms, this would provide a shorter path to arrange the given growth rates from slowest to faster (although at time it will fail, so you need to use *Limit Rule* to verify).

*Constant << Logarithmic << Polynomial << Exponential << Factorial << n power n*  
  
The above order of functions show the relative order of function in increasing order of complexity. It is, however, by no means a definitive indicator that any functions should follow the given order.

## First Things:  

### **Searching**

### I:  

The first algorithm that I learnt was searching. First searching would always be in a random collection of data. Since random collection have no ordering (thus the name random), a simple search should be done where you start at the first element of the array or collection, check to see if that is what you want. If it is what you want, return with the information on how to find the element item again. If not, move on to the next one.  

I have implemented this in a fully runnable python program with a random collection (I have taken a list of integers). Some extra stuffs have been added for obvious correctness verificaiton.

```python
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
```
 
### II:

What is the array was sorted, and we  were required to search element in the sorted array. Obviously, breaking down the array into two halves and searching the item in one of the half would make the job a lot easier. So, I present here the so called Binary Search algorithm.  

```python
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
```

An easier way to remember the complexity of Binary Seach algorithm is to watch that the array or our search space is divided into two halves every iteration. This makes it go for log2(length of array) time. Thus it is log2(n) algorithm.

### **Sorting**

Another indspensible part of algorithms study is the study of sorting algorithm. Following presents the sorting algorithms that we studied. 

### I:

The basic of all the sorting is **Selection Sort**. This would be the sorting algorithm that we might come up with when we wrote our first sorting algorithm. Basically, what is done here is that we find the minimum item from the list and place it in the starting position. We do this operation for as many times as there are elements in the array -1 each time leaving out the first element from the list. eg. a[1........n],a[2....n],a[3.....n] etc  

```python
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
```
Selection Sort is O(n^2) in average.

### II:

Following the same idea as in selection sort, there is another algorithm called **Insertion Sort** where we take an element, finds its place in the sublist indexed from beginning to its position, and insert it there. Of course, it the elements place is somewhere before its position, all the element from the new position to the current index of the element has to shited one place to the right, and then we can insert the element to its appropriate position. That is why its called Insertion Sort.

```python
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
```

### III:

Then comes the **QuickSort**, the most popular of all algorithms. This is more popular because of the idea behind its implementation. It goes as: take an element, make sure all the elements to the left of it are smaller or equal to it , make sure all the elements to the right of it are larger or equal to it. Perform this operation for all the elements in the array.  

Obviously,  the question arises where and how do I choose the element. There are many implementations or idea for that. We can choose the first of all elements are the *pivot*, bring all the lesser or equal elements to the left of it (we may have to move the first element to the right). After this operation is done, the element (first element in previous array) now is in its right place since all the elements to the left of it are smaller or equal and all the elements to the right of it are larger or equal. This leaves us with task of sorting the left half and the right half. In each of these we perform the same operation.

Following given implementation takes the first element as pivot in function *quick_sort_help*, places it in its right position and gives out the index of the right position.

```python
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
```

### IV: 

**Mergesort** works in the concept that we already have sorted lists or arrays, and our task is to merge these two arrays into one. How to find these two in a completely unsorted list of numbers the tricky part here. So the algorithm goes down to dividing the array so that we have a single element in each individual list, merge two of them, and merge two such obtained arrays and so on until we operate with all of them.

```python
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
```
Both Quicksort and mergesort are O(nlogn) algorithm, but since mergesort is not in place algorithm, Quicksort is preferred more than Mergesort.

### V

Sorting algorithms that follows are now non-comparison based algorithms. I will mention about three such algorithms. 
The first in the lot is **Counting Sort**. Here basically what we do is count the number of elements present in the array with a particular value, and based on this we rearrange them in increasing order. For this the counting array is used that increases the count-value in it based on the value of the array detected. This means: if value in array to be sorted is 3, we increase the count value in counting array at index 3 by 1. Following presents the implementation of counting sort.

```python
import random
def countingSort(myList,max_val):
	# the important consideration here is that the values in the array myList are
	# .. from 0 and some know highest value
	return_list = [0]*(len(myList)+1)
	counting_list = [0]*(max_val+1)

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
	max_val = num_elements-1
	myList = random.sample(range(max_val+1),num_elements);

	print("The un-sorted array is :")
	print(myList)
	myList = countingSort(myList,max_val)
	print("The sorted array is :")
	print(myList)
```
Another in the sequence is **Radix Sort**. In radix sort the idea is that you look at the lowest digit (or bit) position, and arrange the numbers based on the order of those digits. Then, go to one position to left and order by that position and so on until you reach the most significant position (or bit).

The number of bit positions is bounded by the largest number we have in the array. One idea will be to take log of the number and perform for that many positions, another approach will be to divide the maximum number by 10 (or the base) each time, and continue until the number is greater than 0. Following implementation will make the concept more clear. Implementation wise, we are going to make use of **Counting Sort** for sorting the numbers based on their positions in iterative way going through all the digit positions.

```python
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
```

### VI

The following algorithm is **HeapSort**. This algorithm changes the algorithm into a data structure called Max Heap (which can be represented as an array), and then performs sorting in thus formed Heap. Following presents the implementation of the complete algorithm starting a complete random input array.

```python
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
```
## Project 1:  
**Project 1** mainly consists of two classes, namely  
 *sortEngine* (inside file helper.py) and  
 *myClass* (inside file main.py).  

-> Class *sortEngine* has a method *quick_sort(array,leftIdx,rightIdx)* which sorts the array in-place.  
-> Class *myClass* has to be initialized with a filename that is to be read.  
   The file consists of numbers that constitutes of a matrix. The first line, however, of the file should mention the number of rows and number of cols in the matrix.  
   *myClass* read the matrix, and using *method1()* of myClass, it sorts all the elements of the matrix, rearranges into the dimensions of the original matrix and prints the final matrix in the output file. The last line of the output file mentions the number of comparisons made and number of assignments done during sorting.  
   Using *method2()*, the matrix is sorted but in a different way. First, each row is sorted. Then each column is sorted. Final matrix is printed in another file in way similar to *method1()*. Both *method1()* and *method2()* make use of *quick_sort(...)*  from *sortEngine*.
->*main()* function prompts user for filename, and calls function *operate()* inside *myClass* which calls *method1()* and *method2()* 
  
## Project 2:  
**Project2** read a file for data and creates optimal binary search tree.  
The input file is named 'input.txt', which is already defined in the code. The nature of file should be such that the first line contains the number of keys desired, and each subsequent lines should be the value of keys (probability)  
It uses the concept of dynamic programming to build the matrix which is used to create the optimal BST  
The matrix generated as well as the final BST is printed to an output file