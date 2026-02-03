#Processing the devices.txt file:

with open('Files_Directories/Project_File_Processing/devices.txt', 'r') as f:
    content = f.read().splitlines()

    new_list = [content[i] for i in range(1,len(content))]
    separated = [data.split(":") for data in new_list]

    print(separated)