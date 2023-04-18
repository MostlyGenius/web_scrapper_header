import requests

url = 'https://example.com'
response = requests.get(url)

# extract relevant information from the response header and store it in a dictionary
data = {}
data['cookies'] = response.cookies
data['headers'] = response.headers

# modify the data as needed
data['cookies']['session_id'] = 'new_session_id'
data['headers']['User-Agent'] = 'Mozilla/5.0'

# print the modified data
print(data)
