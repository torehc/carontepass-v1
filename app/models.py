# -*- coding: utf-8 -*-
from app import db

class Group(db.Model):
    __tablename__ = 'cp_group'

    id_group = db.Column(db.Integer, primary_key=True)
    name_group = db.Column(db.String(120))
    url = db.Column(db.String(160))

    def __str__(self):
        return self.name_group

class User(db.Model):
    __tablename__ = 'cp_user'

    id_user = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    rol = db.Column(db.Enum('adm', 'usr', name="user_rol"), default='usr', nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('cp_group.id_group'))
    group = db.relationship('Group',
        backref=db.backref('users', lazy='dynamic'))
    phone = db.Column(db.String(18))
    address = db.Column(db.String(220))
    email = db.Column(db.String(180))

    def full_name(self):
        return '{} {}'.format(self.name, self.last_name)

    def __str__(self):
        return u'{}, {} ({})'.format(self.last_name, self.name, self.email)

    def get_payment(self, month, year):
        return Payment.query.filter_by(user=self, year=year, month=month).first()

class Message(db.Model):
    __tablename__ = 'cp_message'

    id_message = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(512))
    user_id = db.Column(db.Integer, db.ForeignKey('cp_user.id_user'))
    ts_send = db.Column(db.DateTime)
    ts_received = db.Column(db.DateTime)

class Payment(db.Model):
    __tablename__ = 'cp_payment'

    id_payment = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    month = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('cp_user.id_user'))
    user = db.relationship('User', backref=db.backref('payments', lazy='dynamic'))
    f_payment = db.Column(db.DateTime)
    amount = db.Column(db.Numeric(10, 2))

    def __str__(self):
        return u'{} {}, pago {}/{} ({:.2f}€)'.format(
            self.user.name, 
            self.user.last_name,
            self.month,
            self.year,
            self.amount,
            )

class Device(db.Model):
    __tablename__ = 'cp_device'

    id_device = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('cp_user.id_user'))
    user = db.relationship('User', backref=db.backref('devices', lazy='dynamic'))
    kind = db.Column(db.Enum('mac', 'nfc', name="device_kind"), nullable=False)
    code = db.Column(db.String(64), nullable=False)

    def __str__(self):
        return 'Device {}:{}'.format(self.kind, self.code)

class Log(db.Model):
    __tablename__ = 'cp_log'

    id_log = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('cp_user.id_user'))
    ts_input = db.Column(db.DateTime())
    ts_output = db.Column(db.DateTime(), default=None)
