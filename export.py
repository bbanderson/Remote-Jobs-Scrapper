import csv
from flask import send_file

def make_csv(database, term):
  file = open(f"{term}.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["Searched Term", "Title", "Company", "Link"])
  wework = database["wework"]
  stack = database["stack"]
  remote = database["remote"]
  # print(wework)
  for job in wework:
    remove_logo_url = list(job.values())[1:]
    writer.writerow([term]+remove_logo_url)
  for job in stack:
    remove_logo_url = list(job.values())[1:]
    writer.writerow([term]+remove_logo_url)
  for job in remote:
    remove_logo_url = list(job.values())[1:]
    writer.writerow([term]+remove_logo_url)
  return