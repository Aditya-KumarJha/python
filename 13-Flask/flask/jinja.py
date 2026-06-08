## Building URL dynamically
## Variable rule
## Jinja 2 Template engine

### Jinja 2 Template Engine
'''
    {{ }} -> expression to print output in html
    {% %} -> conditions, for loops
    {# #} -> comments
'''

from flask import Flask, render_template, request, redirect, url_for

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

# @app.route("/submit", methods=["GET", "POST"])
# def submit():
#     if request.method == "POST":
#         name = request.form["name"]
#         return f"Hello {name}!"
    
#     return render_template("form.html")

## Variable rule
# @app.route("/success/<int:score>")
# def success(score):
#     return "The person has passed with " + str(score) + " marks"
@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"
    return render_template("result.html", result=res)

@app.route("/successres/<int:score>")
def successres(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"
    
    exp = {
        "score": score,
        "result": res
    }
    return render_template("result1.html", result=exp)

## if condition
@app.route("/successif/<int:score>")
def successif(score):
    return render_template("result2.html", result=score)

@app.route("/fail/<int:score>")
def fail(score):
    return render_template("result2.html", result=score)

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        science = float(request.form["science"])
        maths = float(request.form["maths"])
        c = float(request.form["c"])
        datascience = float(request.form["datascience"])

        total_score = (science + maths + c + datascience) / 4

        return redirect(url_for("successres", score=int(total_score)))

    return render_template("getresult.html")

if __name__ == "__main__":      # Entry point of any entire code 
    app.run(debug=True)