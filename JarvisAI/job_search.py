"""
Module for job search assistance.
"""

import requests
from bs4 import BeautifulSoup

class JobSearch:
    def __init__(self):
        self.base_url = "https://www.indeed.com/jobs"

    def search_jobs(self, query, location=""):
        params = {
            'q': query,
            'l': location
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            jobs = []
            for div in soup.find_all('div', attrs={'class': 'jobsearch-SerpJobCard'}):
                title = div.find('a', attrs={'class': 'jobtitle'})
                company = div.find('span', attrs={'class': 'company'})
                if title and company:
                    jobs.append(f"{title.text.strip()} at {company.text.strip()}")
            return jobs
        else:
            return ["Error: Could not fetch job listings."]
