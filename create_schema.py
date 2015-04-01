#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String, DateTime

metadata = MetaData()
ca_message = Table('ca_message', metadata,
                Column('id_message', Integer, primary_key=True),
                Column('text', String(512)),
                Column('user_id', Integer),
                Column('ts_send', DateTime()),
                Column('ts_received', DateTime()),
                ) 
print(ca_message)

from sqlalchemy import create_engine
engine = create_engine('postgresql://control_anden:control_anden@192.168.1.94:5432/control_anden')
result = engine.execute('select * from ca_group')
for row in result:
    print(row)
