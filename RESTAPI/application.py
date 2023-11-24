from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is REST API'

@app.route('/outcomes')
def outcomes():
    return 'There are so many goofy outcomes'

