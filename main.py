import requests
from bs4 import BeautifulSoup

url = 'https://weworkremotely.com/categories/remote-full-stack-programming-jobs'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

job_listings = soup.find_all('li', class_='new-listing-container feature')

for job in job_listings:
    company_name = job.find('p', class_='new-listing__company-name').text
    title = job.find('h3', class_='new-listing__header__title').text
    job_link = 'https://weworkremotely.com' + job.find('a', class_='listing-link--unlocked').attrs['href']
    print(company_name, title, job_link)