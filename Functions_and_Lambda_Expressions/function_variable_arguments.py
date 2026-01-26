#Function Variable-Length Arguments: *args, **kwargs

#*args example: allows you to input multiple arguments as a tuple
def calculate_total_cost(base_cost, *args):
    print(args)
    return base_cost + sum(args)

print(calculate_total_cost(10 , 5, 2, 6, 7))



# **kwargs: allows a function to accept any number of keyword arguments
# (arguments passed as key=value)
def display_user_info(**user_data):
    for key, value in user_data.items():
        print(f'{key} => {value}')