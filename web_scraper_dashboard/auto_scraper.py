import json
from web_scraper_dashboard.extract_jobs import scrape_jobs

def save_jobs_to_json(jobs):
    with open('data.json', 'w') as f:
        json.dump(jobs, f, indent=4)

def job_scraper():
    print("Starting scraping jobs")
    jobs = scrape_jobs()
    save_jobs_to_json(jobs)
    print("Scraping completed")
