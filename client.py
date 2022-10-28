import requests

response = requests.post('http://127.0.0.1:5000/advertisement', json={'heading':'zagolovok', 'description': 'text', 'owner': 'Vasya'},)
print(response.status_code)
print(response.text)
print('****')

# response = requests.get('http://127.0.0.1:5000/advertisement/5')
# print(response.status_code)
# print(response.text)
# print('****')

# response = requests.patch('http://127.0.0.1:5000/advertisement/5', json={'heading':'zagolovok5'})
# print(response.status_code)
# print(response.text)
# print('****')
#
# response = requests.get('http://127.0.0.1:5000/advertisement/5')
# print(response.status_code)
# print(response.text)
#
# response = requests.delete('http://127.0.0.1:5000/advertisement/5')
# print(response.status_code)
# print(response.text)
#
# response = requests.get('http://127.0.0.1:5000/advertisement/5')
# print(response.status_code)
# print(response.text)