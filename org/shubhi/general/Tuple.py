#initialize tuple
'''
my_tuple=()
my_tuple_2=tuple()
print(my_tuple)
print(my_tuple_2)
my_tuple=my_tuple + (1,2,3)
print(my_tuple)

#initializing elements to the tuple

my_tuple=(1,2,3)
my_tuple_2 =tuple(('Python','for','edureka'))
print(my_tuple)
print(my_tuple_2)
my_tuple_3 ='example',  # add comma in the end if you want a tuple with single element esle it gives a String
print(type(my_tuple_3))
'''
'''
# Accessing elements of a tuple
my_tuple= (1,2,3)
my_tuple_2 = ('Python','for','edureka')
my_tuple_3 = (1,2,3,['hindi','python'])
print(my_tuple[0])
print(my_tuple_2[:])
print(my_tuple_3[3][1])
'''
# elements in the tuple can be changed if the data type in the list is mutable. Data inside list can be changed but whole tuple elements cannot be changed
my_tuple_3 =(1,2,3,['hindi','python'])
my_tuple_3[3][0] ='english'
print(my_tuple_3)

#tuple methods
print(my_tuple_3.count(2))
print(my_tuple_3.index(['english','python']))
