# python3

import sys
import threading
import numpy as np


def compute_height(a,list,l,ss):
    # print("a:", a)
    # print("list:", list)
    # print("l:", l)
    # print("ss:", ss)
    def func(a):
        if (a in list):
            for i,j in enumerate(list):
                if j==a:
                    l.append(i)

                    func(i)
                    
                    height = len(l) + 2
                    if (height > ss[-1]):
                        ss.append(height)

        if(not len(l)==0):
            l.pop()
    
    func(a)
    # print("height:",ss[-1])
    print("height=",ss[-1])



def main():
    # implement input form keyboard and from files

    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision

    # input number of elements
    # e = input()
    e = 5

    # input values in one variable, separate with space, split these values in an array
    # v = input()
    v = "3 57 29 54 29 94 88 57 40 16 72 16 80 63 89 4 77 77 16 65 72 14 94 82 80 49 69 54 1 99 50 18 52 36 49 50 80 42 89 31 4 52 52 77 88 42 97 73 73 82 88 37 69 63 40 99 36 76 1 37 28 57 82 93 54 63 76 14 18 -1 76 42 14 72 97 28 37 65 99 29 97 3 3 93 65 93 89 40 31 36 73 18 4 49 28 69 1 50 31 94"
    list = []
    
   
    # makes list from input
    number = ""
    for i,j in enumerate(v):
        number = number + j
        if(j == ' '):
            list.append(int(number))
            number = ""
            continue
        if(len(v)-1 == i):
            list.append(int(number))
    # print(list)

    #finds first value
    for i,j in enumerate(list):
        if j == -1:
            a = i

    l = []
    ss = [0]

    compute_height(a,list,l,ss)




            
        
    
    
    # call the function and output it's result

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()

# print(numpy.array([1,2,3]))