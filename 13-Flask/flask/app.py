from flask import Flask

'''
    app = Flask(__name__)
    It creates an instance of the Flask class
    which will be our WSGI (Web Server Gateway Interface) application.
'''
### WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this best Flask Tutorial. This is the best course"

@app.route("/index")
def index():
    return "Welcome to the index page"

if __name__ == "__main__":      # Entry point of any entire code 
    app.run(debug=True)