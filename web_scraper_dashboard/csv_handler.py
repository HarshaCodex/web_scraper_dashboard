import csv

from web_scraper_dashboard.constants import company_header, job_header, link_header


def write_to_csv(data, file):
    with open(file, 'w', newline='') as csvfile:
        field_names = [company_header, job_header, link_header]
        writer = csv.DictWriter(csvfile, fieldnames=field_names)

        writer.writeheader()
        writer.writerows(data)