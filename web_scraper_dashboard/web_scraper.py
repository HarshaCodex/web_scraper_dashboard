import requests

def scraper(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error occurred while calling the url:{e}")
