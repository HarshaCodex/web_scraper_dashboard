from constants import company_field, title_field, link_field, company_header, job_header, link_header, main_url


def extract_jobs(job_listing):
    company_name = job_listing.find('p', class_=company_field).text.strip()
    title = job_listing.find('h3', class_=title_field).text.strip()
    job_link = main_url + job_listing.find('a', class_=link_field).attrs['href']
    return {company_header: company_name, job_header: title, link_header:job_link}
