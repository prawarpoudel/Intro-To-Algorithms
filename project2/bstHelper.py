import os.path
import sys

debug = False
class bst:
	def read_file(self,filename):
		'''
		This function takes a filename as argument.
		The file should have numeric values such that:
			->first line contains the number of 'keys' for BST
			->following other lines contain value of 'keys' for BST
		return value is True/False
		'''
		filename = str(filename)
		# check if the file exists
		if not os.path.isfile(filename):
			print('File {} not found'.format(filename))
			return False
		# if it does, then read the number of items
		f=open(filename,'r')
		if not f:
			print('File Open unsuccessful'.format(filename))
			return False
		# read the whole file at once, we will postprocess later
		# file_contents is a list
		file_contents = [line.strip('\n') for line in f]
		if debug:
			print("Content read from file are \n{}".format(file_contents))

		self.num_keys = int(file_contents[0])
		self.key_list = [int(i) for i in file_contents]

		if debug:
			print('Number of keys mentioned is {}'.format(self.num_keys))
			print('The keys are {}'.format(self.key_list[1:]))

		# checking to see if it is correct
		if not len(self.key_list[1:])==self.num_keys:
			print('Mismatch in number of keys vs actual number given')
			return False

		return True

	def optimalBST(self):
		'''
		This function calculates the optimal BST for the given array of keys.
		It uses the concept of dynamic programming, and fills a 2D matrix

		return  value is True/False
		'''

		# finding the max value just in case, not to use infinity
		inf_val = sum(self.key_list)*2

		if self.num_keys<=0:
			print("Inappropriate number of keys: {}".format(self.num_keys))
			return False

		if not self.num_keys==len(self.key_list[1:]):
			print('Number of keys mentioned is not equal to actual numnber of keys supplied')
			return False

		# create a 2D array for the dynamic programming matrix for optimal BST
		# this follows the algorithm that is discussed in class with very little modification
		# we want rows indexed from 1 to num+1, but we will create 0 to num+1 anyway
		# we want columns indexed from 0 to num
		each_row = [0]*(self.num_keys+1)
		s = list()	# s is the matrix for dynamic programming value
		r = list() 	# r is the matrix for dynamic programming root

		for i in range(self.num_keys+2):
			s.append([0]*(self.num_keys+1))
			r.append([0]*(self.num_keys+1))

		for i in range(1,self.num_keys+1):
			s[i][i] = self.key_list[i]
			r[i][i] = i

		for d in range(1,self.num_keys):
			for i in range(1,self.num_keys-d+1):
				j = i+d
				sum_p = 0
				min_val = inf_val
				min_root = 0
				for k in range(i,j+1):
					sum_p +=self.key_list[k]
					value = s[i][k-1]+s[k+1][j]
					if value<min_val:
						min_val = value
						min_root = k
				s[i][j] = sum_p+min_val
				r[i][j] = min_root

		self.optimal_values = s
		self.optimal_root = r
		return True

	def printDP_toFile(self,f):
		'''
		This function prints the calculated optimal_values matrix to a file named 'pp0030.txt'
		'''
		if not self.optimal_values:
			print('The matrix is not found. Please check')
			return False
		if not self.optimal_root:
			print('The root matrix is not found. Please check')
			return False

		f.write('Table:\n')
		f.write(' {0:4s}|'.format('----'))

		# this prints the first line in output file
		for i in range(1,self.num_keys+1):
			f.write(' {0:8s}'.format(' '))
			f.write('{0:02d}|'.format(i))
		f.write('\n')

		for i in range(1,self.num_keys+1):
			f.write(' {0:2s}'.format(' '))
			f.write('{0:02d}|'.format(i))

			# for the lower diagonal portion, we do not want to print any value
			for j in range(1,i):
				if j==i-1:
					f.write(' {0:9s}'.format(' '))
					f.write('0|')
				else:
					f.write(' {0:10s}|'.format(' '))

			for j in range(i,self.num_keys+1):
				f.write(' {0:6d}('.format(self.optimal_values[i][j]))
				f.write('{0:02d})|'.format(self.optimal_root[i][j]))
			f.write('\n')

	def print_tree(self,i,j,space_needed,f):
		if i<=j:
			for sp in range(space_needed):
				f.write('\t')
			f.write('{0:2d}\n'.format(self.optimal_root[i][j]))
			space_needed += 1

			hasLeftChild = True if (i<=self.optimal_root[i][j]-1) else False
			hasRightChild = True if (self.optimal_root[i][j]+1<=j) else False

			if hasLeftChild:
				self.print_tree(i,self.optimal_root[i][j]-1,space_needed,f)
			elif hasRightChild:
				for sp in range(space_needed):
					f.write('\t')
				f.write(' -\n')

			if hasRightChild:
				self.print_tree(self.optimal_root[i][j]+1,j,space_needed,f)
			elif hasLeftChild:
				for sp in range(space_needed):
					f.write('\t')
				f.write(' -\n')

	def print_BST(self,f):
		'''
		This function prints the optimal binary tree to a file named 'pp0030.txt'
		'''
		if not self.optimal_values:
			print('The matrix is not found. Please check')
			return False
		if not self.optimal_root:
			print('The root matrix is not found. Please check')
			return False

		f.write('Binary Tree:\n')
		self.print_tree(1,self.num_keys,0,f)