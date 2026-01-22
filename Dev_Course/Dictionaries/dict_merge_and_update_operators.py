#Dictionary merge (|) and update (|=) operators:

dict1 = {'a': 1, 'b': 2}
dict2 = {'b':3, 'c': 4}
merged_dict = dict1 | dict2 # | (pipe) combines two dictionaries
print(merged_dict)


#|= update:
dict1 |= dict2 #this operator updates the left hand side dictionary with the keys and values of the right hand side dict
print(dict1)