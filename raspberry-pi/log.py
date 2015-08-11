#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
import sqlalchemy
import datetime
import requests
import json
import time

import sys
sys.path.append("..")

from app import db
from app import models

import telegram
from config import database

engine = create_engine(database)

result = engine.execute('select * from cp_log') 
  

def log_in(user_id):
  
  date = datetime.datetime.now()
  
  log = models.Log(
      user_id = user_id,
      ts_input = date,
      #ts_output = date,
    )
    
  db.session.add(log)
  db.session.commit()
  print(u'[OK ENTRA]')
  print date
  
  
  
  
def log_out(user_id):
  
    lose = models.Log.query.filter_by(user_id=user_id,ts_output=None).first()
    #lose = models.Log.query.filter_by(user_id=user_id).first()
    
    date = datetime.datetime.now()

    lose.ts_output = date
    
    db.session.commit()
    
    print(u'[OK SALE]')
    
  
  

def log_time(user_id):
    
    lose = models.Log.query.filter_by(user_id=user_id).first()
  
    time = (lose.ts_output) - (lose.ts_input)
    print(u'[TIEMPO DENTRO]')
    print time
    

def log_user(user_id):
  
    lose = models.Log.query.filter_by(user_id=user_id,ts_output=None).first()
    
    if lose == None:
      log_in(user_id)
      
    elif lose.ts_output == None:
      log_out(user_id)
      log_time(user_id)
      
    else:
      log_in(user_id)
 
    
def log_first():
  
    lose = models.Log.query.filter_by(ts_output=None).all()
    if len(lose) == 0:
      telegram.send_group_msg(False)
    elif len(lose) == 1:
      telegram.send_group_msg(True)
      
      
def log_persons():
  
    lose = models.Log.query.filter_by(ts_output=None).all()
    return len(lose)
   
def users_in_place():
    rows = models.Log.query.filter_by(ts_output=None).all()
    result = [
        models.User.query.get(r.user_id)
        for r in rows
        ]
    return result
          
    
    
   

