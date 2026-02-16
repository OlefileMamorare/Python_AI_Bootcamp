# Writing To Text Files

with open('Files_Directories/myfile.txt', 'w') as f:
    f.write('Just a line.\nJust a second line.\n')

with open('Files_Directories/myfile.txt', 'a') as f:
    f.write('Some text here.\n')



# 'r+' parameter adds content to the beginning of the file:
with open('Files_Directories/myfile.txt', 'r+') as f:
    f.write('Hello World.\n')