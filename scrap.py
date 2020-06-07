import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def so(term):
  print(f"Start scrapping {term} on StackOverFlow...")
  url = f"https://stackoverflow.com/jobs?r=true&q={term}"
  result = requests.get(url, headers=headers)
  soup = BeautifulSoup(result.text, "html.parser")
  divs = soup.find_all("div", {"class": "-job"})
  jobs = []
  for div in divs:
    if div.find("img", {"class": "grid--cell"}):
      avatar_url = div.find("img", {"class": "grid--cell"})["src"]
    else:
      avatar_url = None
    title = div.find("h2").find("a")["title"]
    company = div.find("h3").find("span").get_text(strip=True)
    link = div.find("h2").find("a")["href"]
    data = {
      "avatar": avatar_url,
      "title": title,
      "company": company,
      "link": f"https://stackoverflow.com{link}"
    }
    jobs.append(data)
  print(f"Scrapping {term} has completed! Total {len(jobs)} jobs on StackOverFlow.")
  return jobs

def wework(term):
  print(f"Start scrapping {term} on WeWork...")
  url = f"https://weworkremotely.com/remote-jobs/search?term={term}"
  result = requests.get(url, headers=headers)
  soup = BeautifulSoup(result.text, "html.parser")
  lis = soup.find_all("li", {"class": "feature"})
  jobs = []
  for li in lis:

    anchors = li.find_all("a")
    for anchor in anchors:
      link = anchor["href"]
      if link[:13] == "/remote-jobs/":
        if li.find("div", {"class": "flag-logo"}):
          avatar_url = li.find("div", {"class": "flag-logo"})["style"][21:-1]
          # print(avatar_url)
        else:
          avatar_url = None
          # avatar_url = "data:image/png;base64,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"
        title = li.find("span", {"class": "title"}).get_text(strip=True)
        company = li.find("span", {"class": "company"}).get_text(strip=True)
        data = {
          "avatar": avatar_url,
          "title": title,
          "company": company,
          "link": f"https://weworkremotely.com{link}"
        }
        jobs.append(data)
  print(f"Scrapping {term} has completed! Total {len(jobs)} jobs on WeWork.")
  return jobs

def remote(term):
  print(f"Start scrapping {term} on Remote...")
  url = f"https://remoteok.io/remote-dev+{term}-jobs"
  result = requests.get(url, headers=headers)
  soup = BeautifulSoup(result.text, "html.parser")
  tds = soup.find_all("td", {"class": "company position company_and_position"})
  jobs = []
  for td in tds:
    link = td.find("a", {"class": "preventLink"})["href"]
    a = soup.find("a", {"href": link})
    # print(a["data-z"])
    # print(a.find("img", {"class": "logo"}))
    try:
      if a.find("img", attrs={"class": "logo"}):
        if a.find("img", {"class": "logo"})["data-src"]:
          avatar_url = a.find("img", {"class": "logo"})["data-src"]

      # avatar_url = a.find("img", {"class": "logo"})['data-src'].get_text()
      # print(avatar_url)
      # else:
      #   continue
    # else:
    #   continue
          company = td.find("h3").get_text(strip=True)
          title = td.find("h2").get_text(strip=True)
          data = {
            "avatar": avatar_url,
            "title": title,
            "company": company,
            "link": f"https://remoteok.io{link}"
          }
          jobs.append(data)
        print(f"Scrapping {term} has completed! Total {len(jobs)} jobs on Remote.")
        return jobs
    except:
      continue

def scrap(term):
  wework_result = wework(term)
  so_result = so(term)
  remote_result = remote(term)
  if wework_result is None:
    wework_result = []
  if so_result is None:
    so_result = []
  if remote_result is None:
    remote_result = []

  total_count = len(remote_result) + len(wework_result) + len(so_result)
  result = {
    "wework": wework_result,
    "stack": so_result,
    "remote": remote_result,
    "total": total_count
  }
  return result
