#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""
import math
n1 = input("Enter 1st number ")
n2 = input("Enter 2nd number ")
n3 = input("Enter 3rd number ")
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
if n1 < n2 and n1 < n3:
    a = n1
    if n2 < n3:
        b = n2
        c = n3
    else:
        b = n3
        c = n2
elif n2 < n1 and n2 < n3:
    a = n2
    if n1 < n3:
        b = n1
        c = n3
    else:
        b = n3
        c = n1
else:
    a = n3
    if n2 < n1:
        b = n2
        c = n1
    else:
        b = n1
        c = n2
if math.sqrt(a * a + b * b) == c:
    print (str(a) + "," + str(b) + "," + str(c) + " form a Pythagorean Triple")
else:
     print (str(a) + "," + str(b) + "," + str(c) + " do not form a Pythagorean Triple")
