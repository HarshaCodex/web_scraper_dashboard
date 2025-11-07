import sqlite3

from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)