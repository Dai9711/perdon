# -*- coding: utf-8 -*-

from telegram.ext import Updater , CommandHandler
import telegram

def start(Update , context) : 

	Update.message.reply_text("Hola")
	
	
	

if __name__ == '__main__':
	
	bot = telegram.Bot(token= "1997378025:AAFYwWKM0dHhKV_JHUl6YTpC_nx6X0nhAVo")
	updater = Updater(token= "1997378025:AAFYwWKM0dHhKV_JHUl6YTpC_nx6X0nhAVo" ,  use_context=True)
	
	update = Updater
	dp = updater.dispatcher
	
	dp.add_handler(CommandHandler('start', start))
		
	updater.start_polling()
	print("Esta Corriendo")
	updater.idle()
	