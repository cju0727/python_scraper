import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
  result = requests.get(URL)

  soup = BeautifulSoup(result.text, "html.parser")

  pagination = soup.find("div", {"class": "pagination"})

  links = pagination.find_all('a')

  pages = []

  for link in links[:-1]:
    pages.append(int(link.string))

  max_page = pages[-1]

  return max_page


def extract_indeed_jobs(last_page):
  jobs = []
  # for page in range(last_page):
  result = requests.get(f"{URL}&start={0*LIMIT}")
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("div", {"class": "heading4"})
  for result in results:
    title = result.find("h2", {"class": "jobTitle"}).find("span", title=True).string
    print(title)

  return jobs
    # print(result.status_code)