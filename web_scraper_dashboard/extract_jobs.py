from bs4 import BeautifulSoup

from web_scraper_dashboard.constants import job_listing_field, company_field, title_field, link_field, job_header, \
    company_header, link_header, main_url, url
from web_scraper_dashboard.web_scraper import scraper


def scrape_jobs():
    response = scraper(url)
    soup = BeautifulSoup(response, 'html.parser')
    job_listings = soup.find_all('li', class_=job_listing_field)

    jobs = list(map(lambda job: extract_jobs(job), job_listings))
    return jobs

def extract_jobs(job_listing):
    company_name = job_listing.find('p', class_=company_field).text.strip()
    title = job_listing.find('h3', class_=title_field).text.strip()
    job_link = main_url + job_listing.find('a', class_=link_field).attrs['href']
    return {company_header: company_name, job_header: title, link_header:job_link}
