#initializing array
'''
a=[]

a.append(10)
a.append(20)
print(a[0])

'''

# convert character to integer

s='4'
c=ord(s)
print("Afetr converting character to integer: %c" %c)

s="10010"  #Start String
c= int(s,2)  # Printing string converting to int base 2
print("After converting to integer base 2: %d" %c)
'''
# Tuple(): ()
s='edureka'
c=tuple(s)
print("After converting String to tuple : ", c,end="\n")
#Set(): {}
c=set(s)
print("After converting String to set : ", c,end="\n")
#List():[]
c=list(s)
print("After converting String to list : ", c,end="\n")
'''

# convert tuple to dictionary
a=1
b=1
tup = (('a',1),('f',2),('g',3))  #initializing tuple

#convert integer to complex number
c=complex(1,2)
print("After converting integer to complex :", c, end="\n")

c=str(a)
print("After converting integer to String : ", c, end="\n")

c=dict(tup)
print("After converting tuple to dictionary : ", c, end="\n")

