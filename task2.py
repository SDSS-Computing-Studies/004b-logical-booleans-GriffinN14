#! python3
# Task2.py

"""
Ask the user to enter a number.
Tell them if the number is both a perfect square and a perfect cube.
(2 points) 

Inputs:
number

Outputs:
xx is both a perfect square and a perfect cube.
xx is only a perfect square.
xx is only a perfect cube.

Example:
Enter a number: 8
8 is only a perfect cube.
"""
import math
ip = input("Enter number ")
ip = int(ip)
ps = math.sqrt(ip)
pc = math.ceil(ip**(1/3))
if int(ps + 0.5) ** 2 == ip and math.pow(pc,3) == ip : 
    print("is both a perfect square and a perfect cube.")
elif int(ps + 0.5) ** 2 == ip:
    print ("is only a perfect square.")
elif math.pow(pc,3) == ip:
    print("is only a perfect cube.")
    else:
    print ("None")
