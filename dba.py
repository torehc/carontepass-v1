#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String, DateTime, Numeric, Enum
from sqlalchemy import ForeignKey
import .config

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

