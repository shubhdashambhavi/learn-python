# genarate array of nrandom numbers
'''
import random

num=5000
inputArray = []

for j in range(num):
    inputArray.append(random.randint(1, 50000))

%%time
bubbleSort = inputArray[:]
 '''

bubbleSort = [5,1,4,2,8,26,]

for i in range(len(bubbleSort)):
    min_index=0
    for j in range(1,len(bubbleSort)):
        if bubbleSort[j]<bubbleSort[min_index]:
            bubbleSort[j],bubbleSort[min_index] = bubbleSort[min_index],bubbleSort[j]

        min_index=j


print("Bubble sort: " , bubbleSort)