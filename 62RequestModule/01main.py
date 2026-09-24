#Requests module in python : The Python Requests module is an HTTP library that enables developers to send HTTP requests in Python. This module enables you to send HTTP requests using Python code and makes it possible to interact with APIs and web services.
#Installation : pip install requests

#To knoe more about it visit "https://requests.readthedocs.io/en/latest/" 
import requests
# response = requests.get("https://www.google.com")
# print(response.text)

url = "https://jsonplaceholder.typicode.com/posts"  #to know placeholder or post visit "jason placeholder"
data = {
    "title" : "Vedant",
    "body" : "bhai",
    "userId" : 12,
}
headers = {
    'Content-type' : 'application/json; charset = UTF-8'
    }
response = requests.post(url, headers = headers, json=data)
print(response.text)
