import os
import requests
# definition of the API address
api_address = os.environ.get('API_ADDRESS', default='localhost:8000')
# API port


# requête
r = requests.get(
    url=f'http://{api_address}/v1/sentiment',
    params= {
        'username': 'alice',
        'password': 'wonderland',
        'sentence': 'life is beautiful'
    }
)

payload = r.json()
score = payload['score']

output = '''
============================
    Content test
============================
request done at "/v1/sentiment"
| username="alice"
| password="wonderland"
| sentence="life is beautiful"
expected result = score > 0
actual result = score -> {score}
==>  {test_status}
'''
# query status
status_code = r.status_code
# display the results
if score > 0:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
output = output.format(score=score, test_status=test_status)
print(output)
# printing in a file
if os.environ.get('LOG') == "1":
    with open('app/logs/api_test.log', 'a') as file:
        file.write(output)

# requête
r = requests.get(
    url=f'http://{api_address}/v1/sentiment',
    params= {
        'username': 'alice',
        'password': 'wonderland',
        'sentence': 'that sucks'
    }
)

payload = r.json()
score = payload['score']

output = '''
============================
    Content test
============================
request done at "/v1/sentiment"
| username="alice"
| password="wonderland"
| sentence="that sucks"
expected result = score < 0
actual result = score -> {score}
==>  {test_status}
'''
# query status
status_code = r.status_code
# display the results
if score < 0:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
output = output.format(score=score, test_status=test_status)
print(output)
# printing in a file
if os.environ.get('LOG') == "1":
    with open('app/logs/api_test.log', 'a') as file:
        file.write(output)

# requête
r = requests.get(
    url=f'http://{api_address}/v2/sentiment',
    params= {
        'username': 'alice',
        'password': 'wonderland',
        'sentence': 'life is beautiful'
    }
)

payload = r.json()
score = payload['score']

output = '''
============================
    Content test
============================
request done at "/v2/sentiment"
| username="alice"
| password="wonderland"
| sentence="life is beautiful"
expected result = score > 0
actual result = score -> {score}
==>  {test_status}
'''
# query status
status_code = r.status_code
# display the results
if score > 0:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
output = output.format(score=score, test_status=test_status)
print(output)
# printing in a file
if os.environ.get('LOG') == "1":
    with open('app/logs/api_test.log', 'a') as file:
        file.write(output)

# requête
r = requests.get(
    url=f'http://{api_address}/v2/sentiment',
    params= {
        'username': 'alice',
        'password': 'wonderland',
        'sentence': 'that sucks'
    }
)

payload = r.json()
score = payload['score']

output = '''
============================
    Content test
============================
request done at "/v2/sentiment"
| username="alice"
| password="wonderland"
| sentence="that sucks"
expected result = score < 0
actual result = score -> {score}
==>  {test_status}
'''
# query status
status_code = r.status_code
# display the results
if score < 0:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
output = output.format(score=score, test_status=test_status)
print(output)
# printing in a file
if os.environ.get('LOG') == "1":
    with open('app/logs/api_test.log', 'a') as file:
        file.write(output)