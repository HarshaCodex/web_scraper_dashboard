import sqlite3

from web_scraper_dashboard.constants import job_header, company_header, link_header


def connect_to_db():
    try:
        connection = sqlite3.connect('job_listings.db')
        cursor = connection.cursor()

        cursor.execute("""
                CREATE TABLE IF NOT EXISTS jobs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    company TEXT,
                    link TEXT UNIQUE
                )
            """)

        connection.commit()
        connection.close()
        print("Connected to database successfully!!!")
    except Exception as e:
        print("Exception occurred:", e)

def save_jobs_to_db(jobs):
    try:
        connection = sqlite3.connect('job_listings.db')
        cursor = connection.cursor()

        for job in jobs:
            cursor.execute(f"""
                    INSERT INTO jobs (title, company, link) VALUES (?, ?, ?)
                """, (job[job_header], job[company_header], job[link_header]))
            connection.commit()

        connection.close()
        print("Jobs saved to database successfully!!!")
    except Exception as e:
        print("Exception occurred while inserting data into table:", e)

def get_jobs():
    try:
        connection = sqlite3.connect('job_listings.db')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM jobs")
        jobs = cursor.fetchall()

        for job in jobs:
            print(job)

        connection.close()
    except Exception as e:
        print("Exception occurred while getting jobs from table:", e)

def delete_jobs():
    try:
        connection = sqlite3.connect('job_listings.db')
        cursor = connection.cursor()

        cursor.execute("DELETE FROM jobs")

        connection.close()
    except Exception as e:
        print("Exception occurred while deleting jobs from table:", e)