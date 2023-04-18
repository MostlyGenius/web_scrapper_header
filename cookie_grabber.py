
import requests

url = 'https://example.com'  # Replace with the desired URL

# Create a session to manage cookies
session = requests.Session()

# Make a request to the website
response = session.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Get all cookies from the session
    cookies = session.cookies.get_dict()

    # Print the cookies
    print("Cookies obtained:")
    for key, value in cookies.items():
        print(f"{key}: {value}")
else:
    print("Failed to fetch the webpage.")
