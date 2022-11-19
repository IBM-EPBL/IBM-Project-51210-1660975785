import requests

NEWS_API_KEY = "333c0c9d6f434ee88b5a622d12397896"

"""def country(country1):
    news_data = requests.get(f'https://newsapi.org/v2/top-headlines?country={country1}&apiKey={NEWS_API_KEY}').json()
    return news_data['articles']"""


def category(arg1, arg2):
    news_data = requests.get(
        f'https://newsapi.org/v2/top-headlines?country={arg1}&category={arg2}&apiKey={NEWS_API_KEY}').json()
    return news_data['articles']


def find(arg3):
    news_data = requests.get(
        f'https://newsapi.org/v2/everything?q={arg3}&apiKey={NEWS_API_KEY}').json()
    return news_data['articles']
