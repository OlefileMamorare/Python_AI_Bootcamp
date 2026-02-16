# Range Expressions (Character Classes)

import re
print(re.findall(r'[aeiouAEIOU]', 'Generative AI'))

#Key patterns:
# [abc]
# [A-Z]
# [a-z]
# [0-9]
# [a-zA-Z] - matches any letter: lowercase or uppercase
# [a-zA-Z0-9_]

print(re.findall(r'[^a-z]', 'Hello, World!, 123345'))