from app import app
from flask import render_template

# views functions
@app.route('/') # decorators
@app.route('/index')
def index():
    user = {'username': 'Juan'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    # return data to jinja2 templates
    return render_template('index.html', title='Home', user=user, posts=posts)