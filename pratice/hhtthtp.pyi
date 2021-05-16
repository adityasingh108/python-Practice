import requests
from requests.exceptions import HTTPError
url = 'https://httpbin.org/'
try:
    response = requests.get(url)
    # If the response was successful, no Exception will be raised
    response.raise_for_status()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
else:
    print('Success!')