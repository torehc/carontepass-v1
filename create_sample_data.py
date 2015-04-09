#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division

import random

from app import db
from app import models
from faker import Factory

def fake_mac_address():
    digits = '0123456789ABCDEF'
    return ''.join([
        random.choice(digits) for _ in range(12)
        ])

def fake_nfc_id():
    digits = '0123456789ABCDEF'
    return ''.join([
        random.choice(digits) for _ in range(7)
        ])

def random_distribute(probs, items):
    acc = 0
    acc_probs = list(probs)
    for i, v in enumerate(probs):
        acc_probs[i] += acc
        acc += v
    n = random.randint(0, acc)
    for (i, v) in enumerate(acc_probs):
        if n <= v:
            break
    return items[i]

def main():
    fake = Factory.create('es_ES')
    fake.seed(1024)
    print(u'Creando datos de ejemplo en la base de datos')
    print(u'  - Creando Grupos')
    grupos = [None]
    for _ in range(3): # Grupos
        grp = models.Group(
            name_group=fake.company(),
            url=fake.url(),
            )
        grupos.append(grp)
        print('    - {}'.format(grp))
    print(u'  - Creando Usuarios')   
    usuarios = []     
    for _ in range(23): # Usuarios 
        usr = models.User(
            name=fake.first_name(), 
            last_name=fake.first_name(), 
            email=fake.email(),
            rol=random_distribute((95, 5), ('usr', 'adm')),
            group=random_distribute((70,10,10,70), grupos),
            )
        print('    - {}'.format(usr))
        usuarios.append(usr)
    print(u'[OK]')
    print(u'  - Creando Dispositvivos')        
    for usr in usuarios: # Usuarios 
        kind = random_distribute((50, 50), ('nfc', 'mac'))
        if kind == 'nfc':
            code = fake_nfc_id()
        else:
            code = fake_mac_address()
        dev = models.Device(user=usr, kind=kind, code=code)
        print('    - {}'.format(dev))
    print(u'[OK]')

if __name__ == '__main__':
    main()








