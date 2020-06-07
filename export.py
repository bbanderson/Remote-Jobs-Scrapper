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
    writer.writerow([term]+list(job.values()))
  for job in stack:
    writer.writerow([term]+list(job.values()))
  for job in remote:
    writer.writerow([term]+list(job.values()))
  return