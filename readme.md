# Description:  
This folder contains multiple projects identified by folder names. Following presents the description of each of the projects in brief.  
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