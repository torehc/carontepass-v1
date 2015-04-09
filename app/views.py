#!/usr/bin/env python

from app import app
from flask import render_template
from app import models

@app.route('/')
@app.route('/index')
def index():
    return 'Hola, mundo'

@app.route('/users')
def users():
    return render_template('users.html', 
        title='Listado de usuarios',
        objects=models.User.query.all(),
        )

@app.route('/users/<id_user>')
def user_detail(id_user):
    id_user = int(id_user)
    user = models.User.query.get(id_user)
    return render_template('user_detail.html', 
        title='{} {}'.format(user.name, user.last_name),
        object=user,
        )   