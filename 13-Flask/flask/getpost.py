from flask import Flask, render_template, request

'''
    app = Flask(__name__)
    It creates an instance of the Flask class
    which will be our WSGI (Web Server Gateway Interface) application.
'''
### WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><body><h1>Welcome to the home page</h1></body></html>"

@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello {name}!"
    
    return render_template("form.html")

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello {name}!"
    
    return render_template("form.html")

if __name__ == "__main__":      # Entry point of any entire code 
    app.run(debug=True)