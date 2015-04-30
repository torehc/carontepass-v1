#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# forms.py

from flask_wtf import Form
from wtforms import StringField, TextField, TextAreaField, SelectField, BooleanField
from wtforms.validators import DataRequired

USER_ROLES = [
    ('usr', u'Usuario'),
    ('adm', u'Administrador'),
    ]

class UserEditForm(Form):
    name = StringField(u'Nombre', validators=[DataRequired()])
    last_name = StringField(u'Apellidos', validators=[DataRequired()])
    email = StringField(u'Correo electrónico')
    phone = StringField(u'Teléfono')
    rol = SelectField(label=u"¿Es Administrador?", choices=USER_ROLES)
    address = TextAreaField(u'Dirección', validators=[DataRequired()])
