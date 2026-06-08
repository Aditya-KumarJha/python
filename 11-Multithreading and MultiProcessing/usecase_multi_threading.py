'''
    Real - Work Example: Multithreading for I/O Bound Tasks
    Scenario: Web Scraping
    Web Scraping often involves making numereous requests to
    fetch web pages. These tasks are I/O bound because they spend a lot of
    time waiting for responses from servers. Multithreading can significantly
    improve the performance by allowing multiple web pages to be fetched concurrently. 
'''

'''
    https://docs.langchain.com/oss/python/langchain/overview
    https://docs.langchain.com/oss/python/langchain/guardrails
    https://docs.langchain.com/oss/python/langchain/frontend/overview
'''

import threading
import requests
from bs4 import BeautifulSoup

urls = [
    "https://docs.langchain.com/oss/python/langchain/overview",
    "https://docs.langchain.com/oss/python/langchain/guardrails",
    "https://docs.langchain.com/oss/python/langchain/frontend/overview"
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f"Fetched {len(soup.text)} characters from {url}")
    print(f"Fetched {url} with title: {soup.title.string}")
    
threads = []
for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()
    
print("All threads have completed fetching content.")