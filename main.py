import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot("6682443785:AAELeiV8qvw-Ps4TehYW3xZVP7liR5_c-3Q")

@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://itproger.com')


@bot.message_handler(commands=["start", "main", "hello"])
def main(message):
    bot.send_message(message.chat.id, f"Hi, {message.from_user.first_name} {message.from_user.last_name}!")

@bot.message_handler(commands=["help"])
def main(message):
    bot.send_message(message.chat.id, "<b>Help</b> <em><u>information</u></em>", parse_mode='html')

@bot.message_handler(content_types=["photo", 'audio'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Go to the website", url='https://itproger.com')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton("Delete photo", callback_data="delete")
    btn3 = types.InlineKeyboardButton("Change text", callback_data="edit")
    markup.row(btn2, btn3)
    bot.reply_to(message, 'So beautiful photo!', reply_markup=markup)

@bot.callback_query_handlers(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
    elif callback.data == "edit":
        bot.edit_message_text("Edit text", callback.message.chat.id, callback.message.message_id)


@bot.message_handler()
def info(message):
    if message.text.lower() == "hi":
        bot.send_message(message.chat.id, f"Hi, {message.from_user.first_name} {message.from_user.last_name}!")
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')



bot.polling(none_stop=True)