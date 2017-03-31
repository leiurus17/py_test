'''
Created on Dec 3, 2016

@author: Marlon_2
'''
# Write a guessing game where the user has to guess a secret number.
# After every guess the program tells the user whether their number was too large or too small.
# At the end the number of tries needed should be printed.
# I counts only as one try if they input the same number multiple times consecutively.

import random

number_to_guess = random.randrange(0,50)

print("Number Guessing Game");
print("Guess the number between")

print(number_to_guess)