'''
Created on Nov 27, 2016

@author: Marlon_2
'''

#Write a program that asks the user for a number n and prints the sum of the numbers 1 to n

number = int(input("Please enter a number: "));
numTotal = 0;
for num in range (0,number+1): #WTF
    #print("num", num);
    numTotal += num;
    #print("numTotal", numTotal);
print("The sum of numbers from 1 to", number, "is", numTotal, ".");