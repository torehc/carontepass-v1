#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String, DateTime, Numeric
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine

import dba


cs = dba.get_connection_string()
engine = create_engine(cs)
dba.metadata.create_all(engine)

if __name__ == '__main__':
    metadata.create_all(engine)
