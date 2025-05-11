import requests

response = requests.get("https://www.google.com")
print(response.status_code)  # Should print 200 if everything works fine
