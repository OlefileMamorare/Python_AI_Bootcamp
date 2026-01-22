# Set and Dictionary Comprehensions


#Set Comprehensions: it is similar to list comprehension

names = {'alice', 'BOB', 'charlie', 'DAVE'}
formatted_names = {name.capitalize() for name in names}
print(formatted_names)

#Dictionary Comprehensions
hyperparams = {'layers': 3, 'units': 256, 'dropout': 0.2}
adjusted_params = {k: v * 2 for k, v in hyperparams.items()}
print(adjusted_params)


updated_params = {k.upper() for k, v in hyperparams.items() if v > 0.2}
print(updated_params)



#zip() function for pairing data:
#used to pair data from 2 different lists into a dictionary
years = [2020, 2021, 2022]
dataset_sizes =[10000, 25000, 50000]
data_growth = dict(zip(years, dataset_sizes))#very important to convert it to a dict
print(data_growth)


#another example of dict comprehension:
sales = {2022: 50000, 2023: 75000, 2024: 100000}
profit = {year: revenue * 0.15 for year, revenue in sales.items()}
print(profit)