'''
Created on Apr 1, 2017

Lists

@author: Marlon_2
'''

fruits = ['avocados', 'apple', 'banana', 'oranges', 'grapes']
print(fruits[0])
print(fruits[0:2])
print(fruits[2:5])

print('mango' in fruits)
print('apple' in fruits)

print('ana' in 'banana')
print('wow' in 'mango')

print('pine' + 'apple')

print('heart ' * 5)

print(", ".join(fruits))
print(fruits)

sep = '; '
print(sep.join(fruits))

vegetables = "carrots, potatoes, onions, leeks, celery"
print(vegetables)
print(vegetables.splitlines())

list(vegetables)
print(vegetables)

print(list('banana'))
print(tuple(vegetables))

vegetables = "carrots, potatoes, onions, leeks, celery, carrots"

vegetables = vegetables.split(', ')

print(len(vegetables))
print(list(vegetables))
print(len(vegetables))

print(vegetables.count("carrots"))
print(max(vegetables))
print(min(vegetables))

print(fruits > vegetables)
print(fruits == fruits)
print(vegetables > fruits)
print(vegetables == fruits)