import requests

api_url = 'https://jsonplaceholder.typicode.com/posts' 


post_data = {
    'title': 'New Post',
    'body': 'This is a new post.',
    'userId': 1
}

try:
    response = requests.post(api_url, json=post_data)
    response_data = response.json()
    
    if response.status_code == 201:
        print("POST Request Successful")
        print("Response:", response_data)
    else:
        print("POST Request Failed")
        print("Status Code:", response.status_code)
        print("Response:", response_data)

except requests.exceptions.Timeout:
    print("TimeOut")
except requests.exceptions.TooManyRedirects:
    print("Try different URL")
except requests.exceptions.RequestException as e:
    raise SystemExit(e)
