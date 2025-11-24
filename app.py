import sqlite3
import threading
import time

import schedule
from flask import Flask, render_template, flash, redirect

from web_scraper_dashboard.db_connection_helper import save_jobs_to_db, delete_jobs
from web_scraper_dashboard.extract_jobs import scrape_jobs

app = Flask(__name__)
app.secret_key = 'supersecretkey'

def job_scraper():
    print("Starting scraping jobs")
    delete_jobs()                 
    save_jobs_to_db(scrape_jobs())
    print("Scraping completed")

def get_jobs():
    try:
        connection = sqlite3.connect('job_listings.db')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM jobs")
        jobs = cursor.fetchall()

        connection.close()
        return jobs
    except Exception as e:
        print("Exception occurred while getting jobs from table:", e)

def schedule_scraper():
    schedule.every(1).day.do(job_scraper)

    while True:
        schedule.run_pending()
        time.sleep(1)

@app.route('/')
def home():
    return render_template('index.html', jobs=get_jobs())

@app.route('/refresh')
def refresh_jobs():
    job_scraper()
    flash("Job listings have been refreshed!")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)