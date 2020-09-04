# python_intro.py
"""Python Essentials: Introduction to Python.
Andrea Dominique O. Cristobal
Data Science Training
August 31, 2020
"""

##Problem 1 & 2
if __name__ == "__main__":
    print("Hello, world!")  
    def sphere_volume(r):
        """Returns the volume of a sphere with radius r"""
        return (4/3)*(3.14159)*(r**3)

print(sphere_volume(5))

"""
Problem 3
Write a function called isolate() that accepts five arguments. 
Print the first three separated by 5 spaces, then print the rest with a single space between each output.
"""

def isolate(a,b,c,d,e):
    """Prints the first three arguments separated by 5 spaces, then print the rest with a single space between each output"""
    print(a,"     ",b,"     ",c,d,e)
    
isolate(1,2,3,4,5)

"""
Problem 4
Write the function first_half() that  should accept a parameter and return the first half of it, excluding the middle character if there is an odd number of characters.
(Hint: the built-in function len() returns the length of the input.)
"""

def first_half(word):
    """Returns the first half of an argument, excluding the middle character if there is an odd number of characters."""
    return word[:len(word)//2] #integer division

print(first_half("odd"))
print(first_half("even"))

#The backward() function should accept a parameter and reverse the order of its characters using slicing, then returns the reversed string.

def backward(word):
    """Reverses the order of an argument's characters using slicing, then return the reversed string."""
    return word[::-1]

print(backward("backward"))
    

"""
Problem 5
Write a function called list_ops(). Define a list with the entries "bear", "ant","cat", and "dog", in that order.
Return the resulting list. Consider printing the list at each step to see the intermediate results.
"""

def list_ops(my_list):
    
    #Append "eagle".
    my_list.append("eagle")
    print(my_list)
    
    #Replace the entry at index 2 with "fox"
    my_list[2] = "fox"
    print(my_list)
    
    #Remove (or pop) the entry at index 1
    my_list.pop(1)
    print(my_list)
    
    #Sort the list in reverse alphabetical order
    my_list.sort(reverse= True)
    print(my_list)
    
    #Replace "eagle" with "hawk"
    my_list[my_list.index("eagle")] = "hawk"
    print(my_list)
    
    #Add the string "hunter" to the last entry in the list
    my_list.append("hunter")
    print(my_list)

    return my_list

print(list_ops(["bear","ant","cat","dog"]))
    

"""
Problem 6
Write a function called pig_latin(). Accept a parameter word, translate it into Pig Latin, then return the translation. 
Specically, if word starts with a vowel, add hay to the end; 
If word starts with a consonant, take the first character of word, move it to the end,and add ay.
"""

def pig_latin(word):
    """"Returns the pig latin translation of a word"""
    if word[0] in 'aeiou':
        return word+'hay'
    else:
        return word[1:]+word[0]+'ay'

print(pig_latin('apple'))
print(pig_latin('kiwi'))
    
"""
Problem 7
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99. 
Write a function called palindrome() that finds and returns the largest palindromic number made from the product of two 3-digit numbers.
"""

def palindrome():
    """"Returns the largest palindromic number made from the product of two 3-digit numbers"""
    value=0
    for n1 in range(100,1000): #3digits
        for n2 in range(100,1000): #3digits
            pal_digit = n1*n2
            string_chk = str(pal_digit) #convert to string to perform indexing
            if string_chk == string_chk[::-1]:
                if pal_digit>value:
                    value=pal_digit
                    continue
    return value

print(palindrome())
    
"""
Problem 8
Write a function called alt_harmonic() that accepts an integer n. 
Use a list comprehension to quickly compute the sum of the first n terms of this series (be careful not to compute only n−1 terms). 
The sum of the first 500,000 terms of this series approximates ln(2) to five decimal places.
"""

def alt_harmonic(n):
    """"Computes the sum of the harmonic sequence for n integers"""
    return sum([((-1)**(n+1))/n for n in range (1,n+1)])

print(alt_harmonic(6))
    