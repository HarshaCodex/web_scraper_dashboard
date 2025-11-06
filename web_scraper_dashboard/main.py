from constants import url, job_listing_field, file
from extract_jobs import extract_jobs
from web_scraper import scraper
from bs4 import BeautifulSoup

from web_scraper_dashboard.db_connection_helper import connect_to_db, save_jobs_to_db, get_jobs, delete_jobs

def main():

    connect_to_db()

    delete_jobs()

    response = scraper(url)
    soup = BeautifulSoup(response, 'html.parser')
    job_listings = soup.find_all('li', class_=job_listing_field)

    jobs = map(lambda job: extract_jobs(job), job_listings)

    save_jobs_to_db(jobs)

    get_jobs()

if __name__=="__main__":
    main()
