# open(filename.txt), read(), write(), close()
#file_object = open('my_txt','a')  to add
file_object = open('my_txt','w')
for text in range(20):
    file_object.write('This is my text. \n')
file_object.close()

count =0
file= open ('my_txt', 'r')
for lines in file:
    count = count + 1
print(count,'lines are present')
file.close()