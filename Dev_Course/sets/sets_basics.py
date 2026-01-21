#A set is an unordered collection of unique, immutable elements

unique_ids = {1 , 2 , 3 , 'a' , 'b ', 4}
unique_ids.add(7)
print(unique_ids)
#empty set:
empty_set = set() # Do Not use empty {} curly braces because this is an empty dictionary

#fozensets
immutable_tokens = frozenset(unique_ids)