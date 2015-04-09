#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String, DateTime, Numeric, Enum
from sqlalchemy import ForeignKey
import config

def get_connection_string():
    return 'postgresql://{usr}:{pwd}@{host}:{port:d}/{db}'.format(
        usr=config.username,
        pwd=config.password,
        host=config.hostname,
        port=config.port,
        db=config.database,
        )

metadata = MetaData()
Base = declarative_base(metadata=metadata)

class Group(Base):
    __tablename__ = 'cp_group'

    id_group = Column(Integer, primary_key=True)
    name_group = Column(String(120))
    url = Column(String(160))

class User(Base):
    __tablename__ = 'cp_user'

    id_user = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    last_name = Column(String(120), nullable=False)
    rol = Column(Enum(['adm', 'usr']), default='usr', nullable=False)
    group_id = ForeignKey('cp_group.id_group')
    phone = Column(String(15))
    address = Column(String(220))
    email = Column(String(180))

class Message(Base):
    __tablename__ = 'cp_message'

    id_message = Column(Integer, primary_key=True)
    text = Column(String(512))
    user_id = Column(Integer, ForeignKey('cp_user.id_user'))
    ts_send = Column(DateTime)
    ts_received = Column(DateTime)

class Payment(Base):
    __tablename__ 'cp_payment'

    id_payment = Column(Integer, primary_key=True)
    year = Column(Integer)
    month = Column(Integer)
    user_id = Column(Integer, ForeignKey('cp_user.id_user'))
    f_payment = Column(DateTime)
    amount = Column(Numeric(10, 2))

class Device(Base):
    __tablename__ 'cp_device'

    id_device = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('cp_user.id_user'))
    kind = Column(Enum(['mac', 'rfc']), nullable=False)
    mac = Column(String(12))
    nfc = Column(String(11))

class Log(Base):
    __tablename__ 'cp_log'

    id_log = Column(Integer, primary_key=True)
    device_id = Column(Integer, ForeignKey('cp_device.id_device'))
    ts_input = Column(DateTime())
    ts_output = Column(DateTime(), default=None)
