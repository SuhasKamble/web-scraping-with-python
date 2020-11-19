import requests
from bs4 import BeautifulSoup
import time
print("Put some unfamiliar skills")
unfamilar_skills = input(">")
print(f"Filtering result for {unfamilar_skills}...\n")

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')

    for job in jobs:
        posted = job.find('span',class_='sim-posted').span.text
        if("few" in posted):
            company_name = job.find('h3',class_='joblist-comp-name').text.replace(" ",'')
            skills = job.find('span',class_='srp-skills').text.replace(' ','')
            more_info = job.header.a['href']
            if unfamilar_skills not in skills:
                print(f'Company Name: {company_name.strip()}')
                print(f'Skills: {skills.strip()}')
                print(f"More Info: {more_info}")
                print("")


if __name__ == '__main__':
    find_jobs()   
    while True:
        find_jobs()
        filter_time = 10
        print(f"Waiting for {filter_time} minute")
        time.sleep(filter_time*60)

           



