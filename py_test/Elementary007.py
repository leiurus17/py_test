'''
Created on Nov 30, 2016

@author: Marlon_2
'''
import sys

#Write a program that prints a multiplication table for numbers up to 12.

print("=== MULTIPLICATION TABLE FROM 1 TO 12 ===\n")

#Print the header
sys.stdout.write("x\t") #So that we can create a proper table
for num in range(1,13):
    sys.stdout.write(str(num) + "\t")
print("");
#Now create the table
for num in range(1,13):
    sys.stdout.write(str(num) + "\t")
    for num2 in range (1,13):
        sys.stdout.write(str(num * num2)+ "\t")
    print("");