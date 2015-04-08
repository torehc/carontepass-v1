#!/usr/bin/env python

from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask
from config import get_connection_string

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = get_connection_string()
db = SQLAlchemy(app)

from app import views
from app import models


