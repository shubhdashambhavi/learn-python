# string splicing

my_str ='Welcome to the tutorial'
'''
print(my_str[:])  # Print all
print(my_str[2:10])  # Print from index 2 until index 9 and skip 10
print(my_str[0:14:1]) # print from index 0 until 13 skipping 1 element
print(my_str[0:14:2])  # print from index 0 to 13 skipping 2 elements
print(my_str[::-1]) # reverse order
print(my_str[-7:-1])
'''

print(len(my_str))  # return length
print(my_str.count('t')) # return length of the string
print(my_str.lower()) # convert to lower case
print(my_str.upper()) # convert to upper case
print(my_str.find('l'))  # returns index of the element found
print(my_str.partition('to'))  # breaks the string into tuple for the element passed
print(my_str.split(' '))  # split the string for the parameter passed
print(my_str.replace('Welcome', 'Hello, welcome')) # replace string with new passed parameter

