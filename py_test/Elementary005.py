'''
Created on Nov 27, 2016

@author: Marlon_2
'''

#Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17

number = int(input("Please enter a number: "))
numTotal = 0

for num in range(1,number+1):
    if num%3 == 0 or num%5 == 0:
        numTotal+=num

print("The sum of the multiples of 3 and 5 from 1 to ", number, "is", numTotal)