from Blogging import app

@app.route('/')
@app.route('/home')
def home():
    return"Home Page"

@app.route('/home')
def login():
    return"Home Page"

@app.route('/home')
def signup():
    return"Home Page"

@app.route('/home')
def account():
    return"Home Page"