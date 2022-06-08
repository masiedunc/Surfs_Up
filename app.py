from flask import Flask

# Flask app instance - "Instance" is a general term in programming to refer to a singular version of something.
app = Flask(__name__) # Variables with underscores before and after them are called magic methods in Python.

# Define the starting point, also known as the root. 
@app.route('/')
def hello_world():
    return 'Hello world'

