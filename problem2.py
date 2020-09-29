#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""
n1 = input("Input number 1 ")
n2 = input("Input number 2 ")
n1 = float(n1)
n2 = float(n2)
if n1 > n2:
    if n1 / n2 == int(n1 / n2):
        print ("is a factor of " + str(n2))
    else:
        print ("is not a factor of " + str(n2))
else:
    if n2 / n1 == int(n2 / n1):
        print ("is a factor of " + str(n1))
    else:
        print ("is not a factor of " + str(n1))
