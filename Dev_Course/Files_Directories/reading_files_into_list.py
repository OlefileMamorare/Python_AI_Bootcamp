#Reading Files Into a List:

# 1. f.read().splitlines(): this splits the string at line boundaries and returns a list composing of those lines:
with open('Files_Directories/config.txt') as f:
    content = f.read().splitlines()
    print(content)


# 2. another method: f.readlines(): reads until the end of the file and returns the list containing the lines:
with open('Files_Directories/config.txt') as f:
    content = f.readlines()
    print(content)

# the readline() reads a single line and moves the cursor to the beginning of the new line.


# 3.
with open('Files_Directories/config.txt') as f:
    content = list(f)
    print(content)

# iterate over the file:
with open('Files_Directories/config.txt') as f:
    for line in f:
        print(line, end='')