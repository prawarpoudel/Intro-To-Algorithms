#!/usr/bin/python3
from tkinter import Tk
from tkinter.filedialog import askopenfilename

from helper import *

class myClass:
    def __init__(self,filename):
        self.filename = filename
        self.comparison_count = 0

    def readFile(self):
        file_handle = open(str(self.filename),'r')
        if file_handle:
            # read the file
            lines = [line.strip('\n') for line in file_handle]

            # create an empty matrix for values to be stored
            self.my_matrix = list()
            
            # find the number of rows and columns
            row_col = [int(val) for val in lines[0].split(' ')]
            self.num_row = row_col[0]
            self.num_col = row_col[1]
            
            # put the values in the matrix from the my_values list
            for each_lines in lines[1:]:
                self.my_matrix.append([float(val) for val in each_lines.split(' ')])

            if self.num_row != len(self.my_matrix):
                print('Mismatch in number of rows. Specified is {}, but found is {}'.format(self.num_row,len(self.my_matrix[0])))
                return False
            elif self.num_col != len(self.my_matrix[0]):
                print('Mismatch in number of columns. Specified is {}, but found is {}'.format(self.num_col,len(self.my_matrix[0])))
                return False

            return True
        else:
            print('Could not open the file with name: '.format(fileName))
            return False
    
    def method1(self):
        my_long_list = list()
        for each_row in self.my_matrix:
            my_long_list.extend(each_row)

        quickSortObject = sortEngine()
        quickSortObject.quick_sort(my_long_list,0,(self.num_col*self.num_row)-1)

        output_file = open('pp0030_1.txt','w')
        output_file.write(str(self.num_row)+' '+str(self.num_col)+'\n')
        for i in range(self.num_row):
            for j in range(self.num_col):
                output_file.write('{0:8.2f} '.format(my_long_list[i*self.num_col+j]))
            output_file.write('\n')
        output_file.write(str(quickSortObject.comparison_count)+' '+str(quickSortObject.assignment_count))
        output_file.close()

    def method2(self):
        my_local_copy = self.my_matrix
        
        quickSortObject = sortEngine()
        
        # sorts each row in place
        for i in range(self.num_row):
            quickSortObject.quick_sort(my_local_copy[i],0,self.num_col-1)

        #first find the transpose of the matrix, and apply similar to above concept
        my_temp = [list(i) for i in zip(*my_local_copy)]
        for i in range(self.num_col):
            quickSortObject.quick_sort(my_temp[i],0,self.num_row-1)
        my_local_copy = [list(i) for i in zip(*my_temp)]
        

        output_file = open('pp0030_2.txt','w')
        output_file.write(str(self.num_row)+' '+str(self.num_col)+'\n')
        for i in range(self.num_row):
            for j in range(self.num_col):
                output_file.write('{0:8.2f} '.format(my_local_copy[i][j]))
            output_file.write('\n')
        output_file.write(str(quickSortObject.comparison_count)+' '+str(quickSortObject.assignment_count))
        output_file.close()

    def operate(self):
        if(self.readFile()):
            # the matrix is read, now perform the task mentioned in the assignment
            if DEBUG_HELPER:
                print("Running Method1 function")
            self.method1()

            if DEBUG_HELPER:
                print("Running Method2 function")
            self.method2()
        else:
            print('Unable to read the matrix. Please follow the error message')
            return

def main():
    # Tk().withdraw()
    # filename = askopenfilename()
    if DEBUG_HELPER:
        print("DEBUG MODE ON: Debug outputs may be seen")
    filename = "input.txt"
    c = myClass(filename)
    c.operate()

# this section calls the main function
if __name__=="__main__":
    main()