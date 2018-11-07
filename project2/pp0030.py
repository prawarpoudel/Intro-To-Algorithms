# This is the program written that creates an optimal binary search tree
# The technique of dynamic programming is used in creating the BST
# The information is received from a file called 'input.txt'

# the way input.txt is written is that:
# .. the first line contains the number of items (keys)
# .. each line thereafter contains the number of times they are seached

from bstHelper import *

if __name__=='__main__':
	
	filename = 'input.txt'

	my_bst = bst()
	my_bst.read_file(filename)
	my_bst.optimalBST()
	
	# open the file in write mode
	f = open('pp0030.txt','w')
	my_bst.printDP_toFile(f)
	my_bst.print_BST(f)