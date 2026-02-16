# Write a function `remove_vowels(s)` that accepts a string and returns a new string
# with all vowels removed (a, e, i, o, u).

def remove_vowels(s):
    vowels = ["a" , "e" , "i" , "o" , "u"]
    new_string = ""

    for char in s:
        if not (char in vowels):
            new_string += char

    return new_string


# Example usage:
print(remove_vowels("jello"))  # 'jll'
print(remove_vowels("sensitivity"))  # 'snstvty'
print(remove_vowels("cellar door"))  # 'cllr dr'

