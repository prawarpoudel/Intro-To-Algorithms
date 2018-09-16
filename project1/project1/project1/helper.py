# this is the helper function that has function names defined to perform some tasks as described in the 
# requirement

class sortEngine:

    def __init__(self):
        self.comparison_count = 0
        self.assignment_count = 0

    def EQ(self,a,b):
        self.comparison_count+=1
        return a==b

    def LT(self,a,b):
        self.comparison_count+=1
        return a<b

    def GT(self,a,b):
        self.comparison_count+=1
        return a>b

    def ASSIGN(self,a,b):
        self.assignment_count+=1
        # since list is mutable
        a[0]=b[0]
        return

    def SWAP(self,a_l,b_l):
        c = [0.0]
        self.ASSIGN(c,b_l)
        self.ASSIGN(b_l,a_l)
        self.ASSIGN(a_l,c)


    def PARTITION(self,array,left,right):
        i = left+1
        j = right
        while(i<=j):
            if not self.GT(array[i],array[left]):
                i+=1
            elif not self.LT(array[j],array[left]):
                j-=1
            else:
                # make a list and pass, since list is mutable
                a_l = [array[i]]
                b_l = [array[j]]
                self.SWAP(a_l,b_l)
                array[i] = a_l[0]
                array[j] = b_l[0]
                j-=1
                i+=1
        
        # make a list and pass, since list is mutable
        a_l = [array[left]]
        b_l = [array[j]]
        self.SWAP(a_l,b_l)
        array[left] = a_l[0]
        array[j] = b_l[0]

        return j

    def quick_sort(self,array,left,right):
        if(left<right):
            pivot = self.PARTITION(array,left,right)
            self.quick_sort(array,left,pivot-1)
            self.quick_sort(array,pivot+1,right)
        return

    def give_values(self):
        return self.comparison_count,self.assignment_count