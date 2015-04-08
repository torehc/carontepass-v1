from app import app

import dba

@app.route('/')
@app.route('/index')
def index():
    return 'Hola, mundo'

@app.route('/users')
def users():
    from app.models import User

    return 'users'+ str(User.query.first())
