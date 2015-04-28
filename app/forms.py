#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# forms.py

from flask_wtf import Form
from wtforms import StringField, TextField, SelectField, BooleanField
from wtforms.validators import DataRequired

class UserEditForm(Form):
    name = StringField('name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    email = StringField('email')
    phone = StringField('phone')
    rol = BooleanField(label=u"¿Es Administrador?")
    address = TextField('address', validators=[DataRequired()])
