#creating Sets
'''
my_set ={1,2,2,3,4,5,5,5}
print(my_set)

#Adding elements in the sets
my_set.add(6)
print(my_set)
'''
#union : adding all elements of both the set
#intersection: finding the common elements of both the set
#difference : (AuB)-B =to delete the common elements and give remaining elements as output
#symmetric difference:(AuB)-(Aintersection Bt)o delete the common elements and give remaining elements as output

my_set= {1,2,3,4}
my_set_2 ={3,4,5,6}

print(my_set.union(my_set_2),'------',my_set |my_set_2)
print(my_set.intersection(my_set_2), '-------', my_set &my_set_2)
print(my_set.difference(my_set_2), '---', my_set - my_set_2)
print(my_set.symmetric_difference(my_set_2), '-----', my_set^my_set_2)
my_set.clear()  # empty the set
print(my_set)
