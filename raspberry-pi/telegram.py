#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from time import sleep
import telebot

TOKEN = '<TOKEN>'
tb = telebot.TeleBot(TOKEN)


def send_simple_msg(message):
  
    IDchatAdmin = 
  
    tb.send_message(IDchatAdmin, message)
  
  
def send_group_msg(SiteOpen):
  
    IDchatGroup = 
    
    if SiteOpen == True:
      tb.send_message(IDchatGroup, "Site Open")
    else:
      tb.send_message(IDchatGroup, "Site Close")