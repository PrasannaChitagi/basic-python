f = open('data.txt', 'r+')

# read the entire file
data = f.read()

# print the data
print(data)

# write the file 
f.write('This is a new line\n')

# close the file 
f.close()
