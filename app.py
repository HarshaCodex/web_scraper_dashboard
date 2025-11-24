import json
from flask import Flask, render_template, flash, redirect
from web_scraper_dashboard.auto_scraper import job_scraper

app = Flask(__name__)
app.secret_key = 'supersecretkey'

def get_jobs():
    try:
        with open('data.json', 'r') as f:
            jobs = json.load(f)
        return jobs
    except (FileNotFoundError, json.JSONDecodeError):
        return []

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