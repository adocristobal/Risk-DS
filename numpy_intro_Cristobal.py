# numpy_intro.py
"""Python Essentials: Intro to NumPy.
Andrea Dominique O. Cristobal
Data Science Training
August 31, 2020
"""
import numpy as np

def prob1():
    """Define the matrices A and B as arrays. Return the matrix product AB."""
    
    A= np.array([[3,-1,4],[1,5,-9]])
    B= np.array([[2,6,-5,3],[5,-8,9,7],[9,-3,-2,-3]])
    return A@B
    raise NotImplementedError("Problem 1 Incomplete")
print(prob1())


def prob2():
    """Define the matrix A as an array. Return the matrix -A^3 + 9A^2 - 15A."""
 
    A= np.array([[3,1,4],[1,5,9],[-5,3,1]])
    return -1*(A**3)+ 9*(A**2)-(15*A)
    raise NotImplementedError("Problem 2 Incomplete")

print(prob2())


def prob3():
    """Define the matrices A and B as arrays. Calculate the matrix product ABA,
    change its data type to np.int64, and return it.
    """
    A= np.triu(np.ones((7,7)))
    B= 5*np.triu(np.ones((7,7)))-np.tril(np.ones((7,7)))-5*np.eye(7)
    mult= A@B@A
    
    return mult.astype(np.float64)
    raise NotImplementedError("Problem 3 Incomplete")

print(prob3())


def prob4(A):
    """Make a copy of 'A' and set all negative entries of the copy to 0.
    Return the copy.

    Example:
        >>> A = np.array([-3,-1,3])
        >>> prob4(A)
        array([0, 0, 3])
    """
    B= np.copy(A)
    mask = B<0
    B[mask] = 0
    
    return B
    raise NotImplementedError("Problem 4 Incomplete")

print(prob4(np.array([-4,-5,3,-1,6])))
    
def prob5():
    """Define the matrices A, B, and C as arrays. Return the block matrix
                                | 0 A^T I |
                                | A  0  0 |,
                                | B  0  C |
    where I is the 3x3 identity matrix and each 0 is a matrix of all zeros
    of the appropriate size.
    """
    
    A= np.array([[0,2,4],[1,3,5]])
    B= 3*np.tril(np.ones((3,3)))
    C= -2*np.eye(3)
    
    v1= np.vstack((np.zeros((3,3)),A,B))
    v2= np.vstack((A.T,np.zeros((5,2))))
    v3= np.vstack(((np.eye(3)),np.zeros((2,3)),C))
    
    block= np.hstack((v1,v2,v3))
    
    return block
    raise NotImplementedError("Problem 5 Incomplete")

print(prob5())

def prob6(A):
    """Divide each row of 'A' by the row sum and return the resulting array.

    Example:
        >>> A = np.array([[1,1,0],[0,1,0],[1,1,1]])
        >>> prob6(A)
        array([[ 0.5       ,  0.5       ,  0.        ],
               [ 0.        ,  1.        ,  0.        ],
               [ 0.33333333,  0.33333333,  0.33333333]])
    """
    
    row_sum= A.sum(axis=1)
    
    return A/row_sum.reshape((3,1))
    raise NotImplementedError("Problem 6 Incomplete")
    
print(prob6(np.array([[1,1,0],[0,1,0],[1,1,1]])))


import os
os.chdir("/Users/mbp15/Documents/Learning/Risk-DS/Python Class/PythonEssentials/NumpyIntro")

def prob7():
    """Given the array stored in grid.npy, return the greatest product of four
    adjacent numbers in the same direction (up, down, left, right, or
    diagonally) in the grid.
    """
    
    grid= np.load("grid.npy")
    
    H=np.max(grid[:,:-3] * grid[:,1:-2] * grid[:,2:-1] * grid[:,3:])
    V=np.max(grid[:-3,:] * grid[1:-2,:] * grid[2:-1,:] * grid[3:,:])
    DD=np.max(grid[:-3,:-3] * grid[1:-2,1:-2] * grid[2:-1,2:-1] * grid[3:,3:]) #diagdown
    DU=np.max(grid[3:,:-3] * grid[2:-1,1:-2] * grid[1:-2,2:-1] * grid[:-3,3:]) #diagup
    
    return max([H,V,DD,DU])
    raise NotImplementedError("Problem 7 Incomplete")

prob7()