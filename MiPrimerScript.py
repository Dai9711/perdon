# -*- coding: utf-8 -*-

from telegram.ext import Updater , CommandHandler
import telegram

def start(Update , context) : 

	Update.message.reply_text("Hola")
	
	
	

if __name__ == '__main__':
	
	bot = telegram.Bot(token= "1959792599:AAG0thQMSTvJ9783vsc5lUkxKeXO-07P2Zo")
	updater = Updater(token= "1959792599:AAG0thQMSTvJ9783vsc5lUkxKeXO-07P2Zo" ,  use_context=True)
	
	update = Updater
	dp = updater.dispatcher
	
	dp.add_handler(CommandHandler('start', start))
		
	updater.start_polling()
	print("Esta Corriendo")
	updater.idle()
	
