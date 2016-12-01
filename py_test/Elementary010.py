'''
Created on Dec 1, 2016

@author: Marlon_2
'''
import datetime

#Write a program that prints the next 20 leap years.
counter = 0;
now = datetime.datetime.now();
current_year = int(now.year);

while counter <= 20:
    if (current_year %4 == 0 and current_year %100 != 0) or current_year %400 == 0:
        print(current_year);
        counter += 1;
    current_year += 1;