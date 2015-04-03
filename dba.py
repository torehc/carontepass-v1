#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config

def get_connection_string():
    return 'postgresql://{usr}:{pwd}@{host}:{port:d}/{db}'.format(
        usr=config.username,
        pwd=config.password,
        host=config.hostname,
        port=config.port,
        db=config.database,
        )
