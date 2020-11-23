from app import app, db
from app.models import User, Post

# creates a shell context that adds the database instance and models to the shell session
@app.shell_context_processor
def make_shell_context():
    # The reason the function returns a dictionary and not a list is that for each item you have 
    # to also provide a name under which it will be referenced in the shell, which is given by the dictionary keys.
    return {'db': db, 'User': User, 'Post': Post}