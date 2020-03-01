#Adding elements into the list

my_list=[1,2,3,'edureka','python']
my_list_2 = list([4,5,3.142,'fun','cool'])
print(my_list)
print(my_list_2)

#Accessing elements of the list

print(my_list[:])  # Accessing all elements of the list
print(my_list[3])  # Accessing the 3rd element of the list
print(my_list[0:4])  # Accessing the elements from 1 to 3, i.e, index 0 to 3 and leaving index 4
print(my_list[::-1])  # Accessing elements in reverse order
print(my_list[0:5:2])  #Access from index 0 to 4 and jumping 2 elements instead of 1
print(my_list[3][2]) # Access particular element of the String edureka (u)

#adding elements to the list
my_list.append([155,12])  #Add passed parameter as a single element
print(my_list)
print(len(my_list))

my_list_2.extend([155,12])
print(my_list_2)
print(len(my_list_2))

my_list.insert(1,'insert_example')  # insert passed parameter in place of index and extend list
print(my_list)

print(my_list + ['just for example'])  # Concatenation
print(my_list * 2)  # Multiply
print(my_list)

