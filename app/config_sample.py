#!/usr/bin/env python
# -*- coding: utf-8 -*-

#~ Database settings

hostname = 'localhost'
port = 5432
username = 'carontepass' 
password = 'carontepass'
database = 'carontepass'

# Máximo número de días del mes que se permite el paso si no se ha pagado
# el mes actual, pero se ha pagado el anterior

MAX_GRANTED_DAYS = 15

# Secret_key is needed to keep the client-side sessions secure.

SECRET_KEY = 'please change this'