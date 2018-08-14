import json
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='ebee3df06f3b482084afedd4e3361716')

response = requests.get('https://newsapi.org/v1/articles?apikey=ebee3df06f3b482084afedd4e3361716&sortBy=latest&source=techcrunch')

articles = json.loads(response)
