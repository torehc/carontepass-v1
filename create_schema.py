#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String, DateTime, Numeric
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine

import dba

metadata = MetaData()
cs = dba.get_connection_string()
print(cs)
engine = create_engine(dba.get_connection_string())

User = Table('cp_user', metadata, autoload=True, autoload_with=engine)
Group = Table('cp_group', metadata, autoload=True, autoload_with=engine)

Message = Table('cp_message', metadata,
                Column('id_message', Integer, primary_key=True),
                Column('text', String(512)),
                Column('user_id', Integer, ForeignKey('cp_user.id_user')),
                Column('ts_send', DateTime()),
                Column('ts_received', DateTime()),
                ) 

Payment = Table('cp_payment', metadata,
	Column('id_payment', Integer, primary_key=True),
	Column('year', Integer()),
	Column('month', Integer()),
	Column('user_id', Integer, ForeignKey('cp_user.id_user')),
	Column('f_payment', DateTime()),
	Column('amount', Numeric(10, 2)),
        ) 

Device = Table('cp_device', metadata,
	Column('id_device', Integer, primary_key=True),
	Column('user_id', Integer, ForeignKey('cp_user.id_user')),
	Column('type', String(3)),
	Column('mac', String(12)),
	Column('nfc', String(11)),
	)   	

Log = Table('cp_log', metadata, 
	Column('id_log', Integer, primary_key=True),
	Column('device_id', Integer, ForeignKey('cp_device.id_device')),
	Column('ts_input', DateTime()),
	Column('ts_output', DateTime(), default=None),
	)

metadata.create_all(engine)