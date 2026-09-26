# Exercise 10 : Use the NewsAPI and the requests module to fetch the daily news related to different topics. Go to: https://newsapi.org/ and explore the various options to build you application

import requests
import json
query = input("What type of news you are interested in? : ")

url = f"https://newsapi.org/v2/everything?q={query}&from=2026-08-26&sortBy=publishedAt&apiKey=9799132a38724fcd940448a99310d850" 

r = requests.get(url)
# print(r.text)

news = json.loads(r.text)
# print(news, type(news))

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")