#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division

from app import db

def main():
    print(u'Eliminando esquema de base de datos', end=':')
    db.drop_all()
    print(u'[OK]')

if __name__ == '__main__':
    main()
    
