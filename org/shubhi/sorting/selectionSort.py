#In every iteration of selection sort,
# the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.

selectionarr= [45,24,12,65,11,9]

for i in range(len(selectionarr)-1):
    min_index=i
    for j in range(i+1,len(selectionarr)):
        if selectionarr[j]<selectionarr[min_index]:
            min_index=j

    selectionarr[i], selectionarr[min_index] = selectionarr[min_index], selectionarr[i]

print("Selection sort: " ,selectionarr )