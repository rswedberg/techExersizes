from flask import Flask, render_template, request
from db import init_db_command
from db_execute import Value
import sqlite3
    
# Create a flask app
def create_app():
  app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static'
  )
  return app

app = create_app()

# Index page
@app.route('/', methods=["GET", "POST"])
def index():
  if request.method == "GET":
    return render_template("index.html")
  else:
    number = int(request.form.get("number"))
    double = number * 2
    Value.create(number, double)
    return render_template("index.html", double=double)

# Retrieve page
@app.route("/retrieve", methods=["GET", "POST"])
def retrieve():
  if request.method == "GET":
    return render_template("retrieve.html")
  else:
    number = request.form.get("number")
    double = Value.get(number)
    return render_template("retrieve.html", double=double)

if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )