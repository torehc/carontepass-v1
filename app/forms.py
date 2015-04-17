from flask_wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

class UserEditForm(Form):
    name = StringField('name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    email = StringField('email')
    phone = StringField('phone')
    rol = SelectField('rol', choices=[
        ('usr', 'Usuario'),
        ('adm', 'Administrador'),
        ])
