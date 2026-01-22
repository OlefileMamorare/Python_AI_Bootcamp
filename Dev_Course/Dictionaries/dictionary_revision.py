#You cannot use a list as a key in a dictionary.
#You can use a tuple instead.

hyperparameters = {
    'learning_rate': 0.0001,
    'dropout_rate': 0.3,
    'optimizer': "Adam",
    'batch_size': 64
}

#adding items to a dictionary:
print(hyperparameters)

#accessing items of a dictionary:
# print(hyperparameters['momentum'])
print(hyperparameters.get('momentum' , 'Not specified'))

#best practices:
#1. Stick to immutable keys
#2. Avoid duplicate keys
#3. Use .get() method for safe access



#Dictionary Operations and Methods: Accessing, Updating, .get(), .keys(), .values():

#Assignment and Copying:
model_params = {'layers': 24, 'units': 512, 'activation': 'relu'}
shared_params = model_params

model_params['activation'] = 'gelu'
print(shared_params)

#Copy
safe_params = model_params.copy()
model_params['layers'] = 48 #does not affect the safe_params variable
print(safe_params)

#Update() method for merging dictionaries:
base_config = {'batch_size': 32, 'epochs': 10}
version_config = {'learning_rage': 0.001, 'units': 128}
base_config.update(version_config)
print(base_config)

#dictionary views with keys(), values(0 , and items()
print(base_config.keys())
print(base_config.values())

#items() returns both keys and values as tuples:
for key, value in base_config.items():
    print(f'{key} => {value}')

#removing items in a dictionary:
#dict.pop(key): removes and returns the key
#dict.popitem(): removes and returns the last item as a tuple
#del dict[key]: removes the key from the dictionary




# Set Operations with Dictionary Keys and Items:

config_a = {'batch_size': 32, 'optimizer': 'adam'}
config_b = {'batch_size': 64, 'optimizer': 'adam', 'momentum': 0.9}

common_keys = config_a.keys() & config_b.keys() # & (ampersand) means intersection
print(common_keys)

#iterate over keys
for key in base_config:
    print(f'Key: {key}')

#iterate over values
for value in base_config.values():
    print(f'Value: {value}')

#iterate over keys and values
for key, value in base_config.items():
    print(f'{key} => {value}')



























