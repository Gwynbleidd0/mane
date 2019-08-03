import config
import telebot
import insta
from telebot import apihelper
from telebot import types
import time


bot = telebot.TeleBot(config.token)
last_test1 = ''
last_test2 = ''

while True:
#    try:
        test = insta.Get_inst('adam_shakhidov')
        if test != last_test1:
            last_test1 = test
            if test[0]:
                bot.send_video('@adamshakhidov',test[1])
                bot.send_message('@adamshakhidov',test[2])
            else:
                bot.send_photo('@adamshakhidov',test[1])
                bot.send_message('@adamshakhidov',test[2])
#    except Exception as er:
#        print(er)
#    try:
        test = insta.Get_inst('trk_put')
        if test != last_test2:
            last_test2 = test
            if test[0]:
                bot.send_video('@trk_put',test[1])
                bot.send_message('@trk_put',test[2])
            else:
                bot.send_photo('@trk_put',test[1])
                bot.send_message('@trk_put',test[2])
#    except Exception as er:
#        print(er)
        time.sleep(60)
if __name__ == '__main__':
		bot.polling(none_stop=True)
