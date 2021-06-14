from flask import Flask, render_template, request

# Create a flask app
app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

# Index page
@app.route('/', methods=["GET", "POST"])
def index():
  if request.method == "GET":
    return render_template("index.html")
  else:
    number = int(request.form.get("number"))
    newNum = number * 2
    message = "Riley chose the number " + str(number) + " and then it doubles to " + str(newNum)
    return render_template("index.html", message=message)

if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )