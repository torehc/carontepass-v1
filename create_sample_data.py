#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division

import decimal
import random
import datetime

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
    print(u'Populate the database with sample data')
    print(u'  - Creating groups')
    grupos = [None]
    for i in range(1, 4): # 3 Grupos
        grp = models.Group.query.get(i)
        if not grp:
            grp = models.Group(
                id_group=i,
                name_group=fake.company(),
                url=fake.url(),
                )
            print(u'    - {}'.format(grp), end=' ')
            db.session.add(grp)
            db.session.commit()
            print(u'[OK]')
        else:
            print(u'    - {}'.format(grp), end=' ')
            print(u'[Skipped]')
        grupos.append(grp)
    print(u'  - Creating users')   
    users = []     
    for i in range(1, 24): # Usuarios 
        usr = models.User.query.get(i)
        if not usr:
            usr = models.User(
                id_user=i,
                name=fake.first_name(), 
                last_name=fake.last_name(), 
                email=fake.email(),
                phone=fake.phone_number(),
                address=fake.address(),
                rol=random_distribute((95, 5), ('usr', 'adm')),
                group=random_distribute((70,10,10,10), grupos),
                )
            print(u'    - {}'.format(usr), end=' ')
            db.session.add(usr)
            db.session.commit()
            print(u'[OK]')
        else:
            print(u'    - {}'.format(usr), end=' ')
            print(u'[skipped]')
        users.append(usr)
    print(u'  - Creating devices')
    for usr in users: # Usuarios 
        if not usr.devices:
            kind = random_distribute((50, 50), ('nfc', 'mac'))
            if kind == 'nfc':
                code = fake_nfc_id()
            else:
                code = fake_mac_address()
            dev = models.Device(user=usr, kind=kind, code=code)
            print(u'    - {}'.format(dev), end=' ')
            db.session.add(dev)
            db.session.commit()
            print(u'[OK]')
        else:
            dev = usr.devices[0]
            print(u'    - {}'.format(dev), end=' ')
            print(u'[Skipped]')
    print(u'  - Creating payments for the current month')
    today = datetime.date.today()
    month, year = today.month, today.year      
    for usr in users: # Usuarios 
        pay = models.Payment.query.filter_by(
            user=usr,
            month=month,
            year=year
            ).first()
        if not pay:
            pay = models.Payment(
                user=usr,
                month=month,
                year=year,
                f_payment=fake.date_time_this_year(),
                amount=decimal.Decimal('10.00'),
                )
            print(u'    - {}'.format(pay), end=' ')
            db.session.add(pay)
            db.session.commit()
            print(u'[OK]')
        else:
            print(u'    - {}'.format(pay), end=' ')
            print(u'[Skipped]')



if __name__ == '__main__':
    main()








