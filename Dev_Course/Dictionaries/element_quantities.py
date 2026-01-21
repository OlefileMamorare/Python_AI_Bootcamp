def element_quantities(quants):
    result = []

    for key in quants:
        for count in range(quants[key]):
            result.append(key)
    return result



quantities1 = {"cat":3,"bird":1,"dog":2 }
print(element_quantities(quantities1))
# ['cat', 'cat', 'cat', 'bird', 'dog', 'dog']

quantities2 = {"blue":3,"brown":1 }
print(element_quantities(quantities2))
# ['blue', 'blue', 'blue', 'brown']

