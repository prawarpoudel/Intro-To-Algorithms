Optimal Binary Search Tree:
=================================
The source code for this project are mentioned in files:
	-> pp0030.py
	-> bstHelper.py

pp0030.py is the main file which makes use of bstHelper.py. All the important stuffs are in bstHelper.py

Operation:
==================================
-> The file "input.txt" is read by the main function in "pp0030.py"
-> It operates on the data to create the optimal binary search tree using the dynamic programming approach
-> Functions called from "bstHelper.py" will print the final dp-table to the file named "pp0030.txt"
-> A function to print the optimal binary tree in the windows directory format is also implemented which will then print the optimal-bst in the same file.

Sample Input:
=================================
8
10
20
40
30
10
20
40
30

Sample Output:
=================================
Table:
 ----|         01|         02|         03|         04|         05|         06|         07|         08|
   01|     10(01)|     40(02)|    110(03)|    170(03)|    200(03)|    270(03)|    390(04)|    480(04)|
   02|          0|     20(02)|     80(03)|    140(03)|    170(03)|    240(03)|    350(04)|    440(04)|
   03|           |          0|     40(03)|    100(03)|    130(03)|    180(04)|    290(04)|    380(04)|
   04|           |           |          0|     30(04)|     50(04)|    100(04)|    190(06)|    260(07)|
   05|           |           |           |          0|     10(05)|     40(06)|    110(07)|    170(07)|
   06|           |           |           |           |          0|     20(06)|     80(07)|    140(07)|
   07|           |           |           |           |           |          0|     40(07)|    100(07)|
   08|           |           |           |           |           |           |          0|     30(08)|
Binary Tree:
 4
	 3
		 2
			 1
			 -
		 -
	 7
		 6
			 5
			 -
		 8

