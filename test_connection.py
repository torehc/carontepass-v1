#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine

engine = create_engine('postgresql://control_anden:control_anden@192.168.1.94:5432/control_anden')

result = engine.execute('select * from ca_group')
for row in result:
    print(row)
