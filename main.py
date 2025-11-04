from constants import url, job_listing_field, file
from csv_handler import write_to_csv
from extract_jobs import extract_jobs
from web_scraper import scraper
from bs4 import BeautifulSoup

def main():
    response = scraper(url)
    soup = BeautifulSoup(response, 'html.parser')
    job_listings = soup.find_all('li', class_=job_listing_field)

    jobs = map(lambda job: extract_jobs(job), job_listings)

    write_to_csv(jobs, file)

if __name__=="__main__":
    main()
