import os.path

class bst:
	def readFile(self,filename):
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
		file_contents = f.readlines()
		self.num_keys = (int)file_contents[0]
		self.key_list = [(int)i for i in file_contents[1:]]

		# checking to see if it is correct
		if not len(self.key_list)==self.num_keys:
			print('Mismatch in number of keys vs actual number given')
			return False

		return True