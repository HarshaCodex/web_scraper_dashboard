import sqlite3

from flask import Flask, render_template, flash, redirect

from web_scraper_dashboard.auto_scraper import job_scraper

app = Flask(__name__)
app.secret_key = 'supersecretkey'

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