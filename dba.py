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

Base = declarative_base()

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
