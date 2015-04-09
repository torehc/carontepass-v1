#!/usr/bin/env python

from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask
from . import config

def get_connection_string():
    return 'postgresql://{usr}:{pwd}@{host}:{port:d}/{db}'.format(
        usr=config.username,
        pwd=config.password,
        host=config.hostname,
        port=config.port,
        db=config.database,
        )

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = get_connection_string()
db = SQLAlchemy(app)

from app import views
from app import models


