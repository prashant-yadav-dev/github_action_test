"""Main application file"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    """Show Homeage"""
    return {"status": "OK"}


@app.route('/<random_string>')
def returnBackwardsString(random_string):
    """Reverse and return the provided URI"""
    reversed_string = "".join(reversed(random_string))
    return {"reversed": reversed_string}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
