'''
Created on Nov 30, 2016

@author: Marlon_2
'''

#Write a program that asks the user for a number n and gives him the possibility to choose between computing the sum and computing the product of 1 to n

sum_total = 0;
product  = 1;

number = int(input("Please enter a number: "));
print("What do you want to do with the number?");
print("[A] Addition");
print("[M] Multiplication");
option = (input("Enter the letter of the option: "));

if option == 'A' or 'a':
    print("Addition");
    
    for num in range(1,number+1): #WTF number+1
        sum_total += num;
        
    print("The sum of the number from 1 to", number, "is", sum_total);
elif option == 'M' or 'm':
    print("Multiplication");
    
    for num in range(1,number+1): #WTF number+1
        product *= num;
    print("The product of the number from 1 to", number, "is", product);
else:
    print("WTF");