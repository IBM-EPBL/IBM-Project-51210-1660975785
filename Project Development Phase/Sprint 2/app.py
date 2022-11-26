from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('signin.html')

@app.route('/signup')
def signup_form():
    return render_template('signup.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/headlines')
def headlines():
    return render_template('notifications.html')

@app.route('/articles')
def articles():
    return render_template('profile.html')

@app.route('/sources')
def sources():
    return render_template('sources.html')


@app.route('/category/business')
def business():
    return  render_template('business.html', sources = sources)

@app.route('/category/tech')
def tech():
    return  render_template('tech.html', sources = sources)

@app.route('/category/entertainment')
def entertainment():
    return  render_template('entertainment.html', sources = sources)

@app.route('/category/science')
def science():
    return  render_template('science.html', sources = sources)

@app.route('/category/sports')
def sports():
    return  render_template('sport.html', sources = sources)

@app.route('/category/health')
def health():
    return  render_template('health.html', sources = sources)

if __name__ == "__main__":
    app.run(debug=True)
