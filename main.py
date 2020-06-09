import os
from flask import Flask, render_template, request, redirect, send_file
from scrap import scrap
from export import make_csv
from add import verify_and_add

app = Flask(__name__)
db = {}
search_list = []

@app.route("/")
def home():
  return render_template("home.html")

# @app.route("/add", methods=["POST"])
# def add():
#   term = request.form["term"]
#   word = verify_and_add(term)
#   print(word)
#   if word:
#     search_list.append(word)
#     return render_template("home.html", items=search_list)
#   else:
#     err_message = "That subreddit does not exist."
#     print(err_message)
    # return render_template("error.html", message=err_message)

def coloring(term):
  term = term.lower()
  color = "#000"
  if "javascript" in term or "node" in term or "deno" in term or "type" in term:
    color = "#F1D91E"
  elif "python" in term or "flutter" in term:
    color = "#3776AC"
  elif "react" in term or "go" in term:
    color = "#5CCAE8"
  elif "git" in term or "shell" in term:
    color = "#D89CF6"
  elif "java" == term or "c" in term:
    color = "#FF9595"
  else:
    color = "#99b898"
  return color

# def calc_len(term, data_list):
#   count = 0
#   for data in data_list:
#     if 



@app.route("/report")
def report():
  raw_terms = request.args.get("term")
  # print(raw_terms)
  if raw_terms == "":
    return redirect("/")
  terms = raw_terms.split(" ")
  # print(terms)
  # for term in terms:

  # remove_space = terms[0].split(" ")
  multiple_term = []
  # print(remove_space)
  for term in terms:
    print(term)
    if term == "":
      continue
    # print(term)
  # term = request.form[""]
    term = term.lower()
    history = db.get(term)
    if history:
      result = db[term]
    else:
      result = scrap(term)
      db[term] = result
    color = coloring(term)
    multiple_term.append({
      "wework":result["wework"],
      # "wework_count":calc_len(result["wework"]),
      "stack":result["stack"],
      # "stack_count":len(result["stack"]),
      "remote":result["remote"],
      # "remote_count":len(result["remote"]),
      "total":result["total"],
      "term":term,
      "color": color
    })
  # print(multiple_term)
  return render_template(
    "report.html",
    terms_list=multiple_term,
    raw_terms=raw_terms,
    # wework_count=len(multiple_term)
    )

@app.route("/export")
def export():
  try:
    term = request.args.get("term")
    # term = term.lower()
    # raw_terms = request.args.get("term")
    # terms = raw_terms.split("+")
    # remove_space = terms[0].split(" ")
    # for term in remove_space:
    # multiple_term = []
    if not term:
      raise Exception()
    # else:
    term = term.lower()
    database = db.get(term)
    if not database:
      raise Exception()
      # else:
    make_csv(database, term)
    # return redirect(f"/export?term={raw_terms}")
    return send_file(f"{term}.csv")
  except:
    return redirect("/")



if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host="0.0.0.0", port=port)
# app.run("127.0.0.1")