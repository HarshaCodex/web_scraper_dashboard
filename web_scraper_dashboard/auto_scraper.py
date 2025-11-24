from web_scraper_dashboard.db_connection_helper import delete_jobs, save_jobs_to_db
from web_scraper_dashboard.extract_jobs import scrape_jobs

def job_scraper():
    print("Starting scraping jobs")
    delete_jobs()
    save_jobs_to_db(scrape_jobs())
    print("Scraping completed")
