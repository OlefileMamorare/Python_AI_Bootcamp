f = open("Files_Directories/config.txt", 'r')
#content = f.read(5)
#print(content)

content = f.read(4)
print(content)




print(f.tell())# tell() method tells you which position the cursor is at

#seek() method: used to move the cursor to a specific location
#seek(0) will move the cursor to the beginning of the file
f.seek(2)
content = f.read(3)
print(content)

print(f.tell())
f.close()