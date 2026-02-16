#varible scope and namespaces
#a namespace is a container that holds names for everything we define - like variables, functions, or classes
# namespaces allow us to use the same name in different parts of our code without causing confusion

# 3 namespaces and scopes in Python:
# 1. Built-in Namespace (Python built-in functions)
# 2. Global (Module Namespace): names define in scripts
# 3. Local Namespace: names defined inside functions


#Built-in Namespace Example
scores = [85, 90, 78, 92]
print(max(scores))

# Global Namespace Example:
accuracy = 0.95#accuracy is in the global namespace
def report_accuracy():
    print(f'Model accuracy is {accuracy * 100}%')

report_accuracy()

