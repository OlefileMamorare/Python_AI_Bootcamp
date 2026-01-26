# Dict Packing and Unpacking

# packing:
def save_user_info(**user_data):
    print(f'User information: {user_data}')

save_user_info(name='Olefile', age=40, location='NYC')


# unpacking:
def connect_to_server(ip, port, username, password):
    print(f'Connecting to {ip}:{port} as {username}')

server_info = {
    'ip': '192.168.0.3',
    'port': 22,
    'username': 'admin',
    'password': 'ajkshdfklja'
}

connect_to_server(**server_info)

# merging dictionaries:
default_settings = {'batch_size': 32, 'learning_rate': 0.001, 'epochs': 10}
experiment_settings = {'batch_size': 64, 'learning_rate': 0.0005}
combined_settings = {**default_settings , **experiment_settings}
print(combined_settings)