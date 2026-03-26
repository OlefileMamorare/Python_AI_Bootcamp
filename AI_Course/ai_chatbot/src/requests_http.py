# The requests Library
import  json
import requests

import httpx

# url = 'https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&hourly=temperature_2m'
# response = requests.get(url)
# print(response.status_code)
#
# print(response.headers)
# print(response.text)
# data = response.json()
# print(data['hourly'])

# r = httpx.get(url)
# print(r.status_code)
# print(r.json())


# Handling requests errors:

try:
    url = 'https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&hourly=temperature_2m'
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    print(json.dumps(response.json(), indent=4))
except requests.exceptions.RequestException as e:
    print(f'An error occurred: {e}')
