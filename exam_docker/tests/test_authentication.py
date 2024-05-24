import os
import requests
# definition of the API address
api_address = os.environ.get('API_ADDRESS', default='localhost:8000')
# API port

print(os.environ.get('LOG') + "log")

# requête
r = requests.get(
    url=f'http://{api_address}/permissions',
    params= {
        'username': 'alice',
        'password': 'wonderland'
    }
)
output = '''
============================
    Authentication test
============================
request done at "/permissions"
| username="alice"
| password="wonderland"
expected result = 200
actual result = {status_code}
==>  {test_status}
'''
# query status
status_code = r.status_code
# display the results
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
output = output.format(status_code=status_code, test_status=test_status)
# printing in a file
if os.environ.get('LOG') == "1":
    with open('app/logs/api_test.log', 'a') as file:
        file.write(output)


# requête
r = requests.get(
    url=f'http://{api_address}/permissions',
    params= {
        'username': 'bob',
        'password': 'builder'
    }
)
output = '''
============================
    Authentication test
============================
request done at "/permissions"
| username="bob"
| password="builder"
expected result = 200
actual result = {status_code}
==>  {test_status}
'''
# query status
status_code = r.status_code
# display the results
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
output = output.format(status_code=status_code, test_status=test_status)
# printing in a file
if os.environ.get('LOG') == "1":
    with open('app/logs/api_test.log', 'a') as file:
        file.write(output)

# requête
r = requests.get(
    url=f'http://{api_address}/permissions',
    params= {
        'username': 'clementine',
        'password': 'mandarine'
    }
)
output = '''
============================
    Authentication test
============================
request done at "/permissions"
| username="clementine"
| password="mandarine"
expected result = 403
actual result = {status_code}
==>  {test_status}
'''
# query status
status_code = r.status_code
# display the results
if status_code == 403:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
output = output.format(status_code=status_code, test_status=test_status)
# printing in a file
if os.environ.get('LOG') == "1":
    print("?SHOULD LOG")
    with open('app/logs/api_test.log', 'a') as file:
        file.write(output)