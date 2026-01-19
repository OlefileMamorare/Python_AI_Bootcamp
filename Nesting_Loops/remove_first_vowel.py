# Write a function `remove_first_vowel(s)` that accepts a string and returns the string
# with its first vowel removed.


def remove_first_vowel(s):


    vowels = ["a" , "e" , "i" , "o" , "u"]
    new_str = ""

    for i in range(len(s)):
        if s[i] in vowels:
            for j in range(i + 1 , len(s)):
                new_str += s[j]

            break

        else:
            new_str += s[i]


    return new_str



# Example usage:
print(remove_first_vowel("volcano"))  # 'vlcano'
print(remove_first_vowel("celery"))  # 'clery'
print(remove_first_vowel("juice"))  # 'jice'

