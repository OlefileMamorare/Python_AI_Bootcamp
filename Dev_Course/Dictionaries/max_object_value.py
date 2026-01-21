def max_object_value(diction):

    values = []
    keys =[]

    for key in diction:
        values.append(diction[key])
        keys.append(key)

    high_value = values[0]

    for i in range(1 , len(values)):
        if values[i] > high_value:
            high_value = values[i]

    high_pair = [keys[values.index(high_value)] , high_value]
    return high_pair

print(max_object_value({"a":5,"b":2,"c":6,"d":7,"e":4 }))
# ['d', 7]

print(max_object_value({"lychee":11,"rambutan":13,"papaya":9 }))
# ['rambutan', 13]
