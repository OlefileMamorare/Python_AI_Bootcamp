# Opening and Reading Files

# open() function opens a file and returns a file object:
# it takes one or 2 arguments: the file name and the Access Mode (Read, Write, Append, etc.)


f = open("Files_Directories/config.txt", "r") # f is a file object. 'r' means READ ONLY
content = f.read()
print(content)

f.close()
print(f.closed)