#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from time import sleep
import telebot
from config import TOKEN
from config import IDchatAdmin
from config import IDchatGroup

tb = telebot.TeleBot(TOKEN)


def send_simple_msg(message):
    
    tb.send_message(IDchatAdmin, message)
  
  
def send_group_msg(SiteOpen, user_name):
  
    if SiteOpen == True:
      tb.send_message(IDchatGroup, site_name+" Open ("+user_name+")" )
    else:
      tb.send_message(IDchatGroup, site_name+" Closed ("+user_name+")" )
   
