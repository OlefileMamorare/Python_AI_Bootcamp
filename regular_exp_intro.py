# Introduction to Regular Expressions (Regex)

import re

# \d : matches any digit (0-9)
# \w : matches any alphanumeric character, including underscore (a-z, A-Z, 0-9, _)
# \s : matches any whitespace character (space, tab, newline)
# . (dot): matches any character except a newline



# Quantifiers:
# + matches one or more occurrences
# * matches zero or more occurrences
# ? matches zero or one occurrences
# {n} matches exactly n occurrences
# {n, m} matches between n and m occurrences

post = 'Exploring the future with #ArtificialIntelligence and #MachineLearning! #AI #GenAI'
hashtags = re.findall(r'#\w+', post)
print(hashtags)


# Using Anchors and Grouping for Precise Matching:
# ^ - matches the start of a string
# $ - matches the end of a string