import random
import pyautogui
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

from key import TOKEN, ID

bot = telebot.TeleBot(TOKEN)







@bot.message_handler(commands=["start"])
def start(message):
    baton = ReplyKeyboardMarkup()
    baton1 = KeyboardButton("/screenshot")
    baton2 = KeyboardButton("/casino")
    baton3 = KeyboardButton("/game_guess_the_number")
    baton.add(baton1, baton2)
    baton.add(baton3)

    bot.send_message(message.from_user.id,
                     "Hi welcome sorry for using english keyboard if you don't understand it i just don't have another keyboard",
                     reply_markup=baton)

@bot.message_handler(commands=["add_note"])
def start(message):
    bot.send_message(message.from_user.id,
                     "what is the note(type the note)")
    bot.register_next_step_handler(message,hjbg)
def hjbg(message):
    bot.send_message(message.from_user.id,
                     "how important is note")
    bot.register_next_step_handler(message,hjbg)

def hgbj(message):
    bot.send_message(message.from_user.id,
                     "your note was added")
bot.polling()


