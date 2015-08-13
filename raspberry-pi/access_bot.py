#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import telebot
from telebot import types
import time
import log

import client_raspberry
from config import TOKEN
from config import IDchatAdmin


commands={ #command description used in the "help" command
#'start': 'Get used to the bot', 
'open': 'Open Door',
'who': 'Who is in there?',
'help': 'Gives you information about the available commands',
}
            
def listener(messages):

	for m in messages:
		chatid = m.chat.id
		print chatid 
		print m.text
		#if m.content_type == 'text':
			#print str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text



bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)



try:
	bot.polling()
except Exception:
	pass
      
      
      
@bot.message_handler(commands=['open']) 
def open_door(m):
  
	chatid = m.chat.id
	
	if chatid == IDchatAdmin:
	    bot.send_message(chatid, 'Opening Door')
	    client_raspberry.action(True)
   	else:
	    bot.send_message(chatid, 'No Access to Door')
	   
@bot.message_handler(commands=['who']) 
def command_who(m):
	chatid = m.chat.id
	users = log.users_in_place()
	
	if not users:
		msg = 'No People'
	else:
		msg = 'People here are: {}'.format(
	  	', '.join([str(u.full_name()) for u in users])
	 	 )

	bot.send_message(chatid, msg) 
	    
@bot.message_handler(commands=['help']) 
def command_help(m):
	chatid = m.chat.id
	helpText = "The following commands are available: \n"
	for key in commands:                  #generate help text out of the commands dictionary defined at the top
		helpText += "/" + key + ": "
		helpText += commands[key] + "\n"
	bot.send_message(chatid, helpText)       #send the generated help page
	

	
while True: 
	try:
		time.sleep(1)
	except KeyboardInterrupt:
		break
