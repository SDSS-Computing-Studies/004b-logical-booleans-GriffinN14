"""
Problem 1
Ask the user to enter a number.
The number is considered frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is frue.
"""

#! python3
ip = input("Enter number ")
ip = float(ip)
if ip / 6 == int(ip / 6) and ip / 8 == int(ip / 8):
    print ("is frue")
else:
    print("is not frue")
