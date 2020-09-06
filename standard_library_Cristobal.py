# standard_library.py
"""Python Essentials: The Standard Library.
Andrea Dominique O. Cristobal
Data Science Training
August 31, 2020
"""


# Problem 1
def prob1(L):
    """Return the minimum, maximum, and average of the entries of L
    (in that order).
    """
    return (min(L),max(L),sum(L)/len(L))
    raise NotImplementedError("Problem 1 Incomplete")

print(prob1([1,2,3,4,5,6])) #Example

# Problem 2
def prob2():
    """Determine which Python objects are mutable and which are immutable.
    Test numbers, strings, lists, tuples, and sets. Print your results.
    """
    
    ##Integers
    int_1= 2
    int_2 = int_1
    int_2 = 3
    
    ##Strings
    str_1 = "andrea"
    str_2 = str_1
    str_2 = "ac"
    
    ##Lists
    list_1 = ['blue','red','white']
    list_2 = list_1
    list_2[1] = 'magenta'
    
    ##Tuples
    my_tuple_1 = (4,5,6)
    my_tuple_2 = my_tuple_1
    my_tuple_2 = my_tuple_1 + (1,)
      
    ##Sets
    set_1 = {1,2,3}
    set_2 = set_1
    set_2.add(4)
    
    if int_1 == int_2:
        result_int= "Numbers are mutable."
    else:
        result_int= "Numbers are immutable."
    
    if str_1 == str_2:
        result_str= "Strings are mutable."
    else:
        result_str= "Strings are immutable."
        
    if list_1 == list_2:
        result_list= "Lists are mutable."
    else:
        result_list= "Lists are immutable."
        
    if my_tuple_1 == my_tuple_2:
        result_tuple= "Tuples are mutable."
    else:
        result_tuple= "Tuples are immutable."
    
    if set_1 == set_2:
        result_set= "Sets are mutable."
    else:
        result_set= "Sets are immutable."
       
    return result_int, result_str, result_list, result_tuple, result_set
    raise NotImplementedError("Problem 2 Incomplete")
    
print(prob2())


# Problem 3
import os
os.getcwd()
os.chdir("/Users/mbp15/Documents/Learning/Risk-DS/Python Class/PythonEssentials/StandardLibrary")

import calculator as calc

def hypot(a, b):
    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any functions other than those that are imported from your
    'calculator' module.

    Parameters:
        a: the length one of the sides of the triangle.
        b: the length the other non-hypotenuse side of the triangle.
    Returns:
        The length of the triangle's hypotenuse.
    """
    
    return calc.sqrt(calc.add(calc.mult(a,a),calc.mult(b,b)))
    raise NotImplementedError("Problem 3 Incomplete")

print(hypot(3,4))


# Problem 4
from itertools import combinations
def power_set(A):
    """Use itertools to compute the power set of A.

    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.

    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    return [subset for r in range(len(A) + 1) for subset in combinations(A, r)]
    raise NotImplementedError("Problem 4 Incomplete")
    
print(power_set(['a','b','c']))


import box
import time
from random import randint

# Problem 5: Implement shut the box.
def shut_the_box(player,timelimit,num):
    """Play a single game of shut the box."""

    