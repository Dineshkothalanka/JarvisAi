"""
Module for performing web search using an API.
"""

import requests

class WebSearch:
    def __init__(self, api_key):
        self.api_key = api_key
        self.search_url = "https://www.googleapis.com/customsearch/v1"

    def search(self, query):
        params = {
            'key': self.api_key,
            'cx': 'YOUR_SEARCH_ENGINE_ID',
            'q': query
        }
        response = requests.get(self.search_url, params=params)
        if response.status_code == 200:
            results = response.json().get('items', [])
            return [item['title'] + ": " + item['link'] for item in results]
        else:
            return ["Error: Could not fetch search results."]
