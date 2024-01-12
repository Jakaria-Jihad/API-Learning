from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is REST API'

@app.route('/outcomes')
def outcomes():
    return 'There are so many goofy outcomes, type outcomes/details for more!'

@app.route('/outcomes/details')
def outcomes_details():
    info = """
    1. I will be more clear about MVC model.
    2. Learn the Python frameworks.
    3. Can start my journey as a developer.
    4. Gonna get a job. hehehehe
    """
    return info
