# with keyword opens the file and closes it automatically without the need to use the close() function.

with open('Files_Directories/config.txt') as file:
    content = file.read()
    print(content)

print(file.closed)
