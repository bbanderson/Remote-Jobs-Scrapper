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
    if list(job.values())[1]:
      continue
    else:
      writer.writerow([term]+list(job.values()))
  for job in stack:
    if list(job.values())[1]:
      continue
    else:
      writer.writerow([term]+list(job.values()))
  for job in remote:
    if list(job.values())[1]:
      continue
    else:
      writer.writerow([term]+list(job.values()))
  return