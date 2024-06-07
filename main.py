import telebot
from telebot import types

API_TOKEN = '7426397411:AAGrdq_ZdTw-ejd5L6wL3_gwl7fuotcv7oY'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Играть")  
    bot.send_message(message.chat.id, '👋', reply_markup=markup)

@bot.message_handler(regexp='играть')
def start_game(message):
    bot.send_message(message.chat.id, "Нажмите на ссылку, чтобы начать игру:")
    bot.send_message(message.chat.id, "http://192.168.1.6:8000/game.html")  # Замените ссылку на актуальную


bot.infinity_polling()
