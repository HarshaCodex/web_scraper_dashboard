import sqlite3

from web_scraper_dashboard.db_connection_helper import connect_to_db, save_jobs_to_db, delete_jobs
from web_scraper_dashboard.extract_jobs import scrape_jobs

from flask import Flask, render_template, flash, redirect

app = Flask(__name__)
app.secret_key = 'supersecretkey'

def job_scraper():
    delete_jobs()                 
    save_jobs_to_db(scrape_jobs())

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