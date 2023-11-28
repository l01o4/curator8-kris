import telebot

bot = telebot.TeleBot('6884432609:AAFB3tvpnbjMbp0Mt12Wu8dKBXvIwfwa0-s')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'ПОКОРМИ МЕНЯ')


@bot.message_handler(commands=['food'])
def main(message):
    bot.send_message(message.chat.id, '*Ням-ням* Спасибо!', parse_mode='Markdown')


@bot.message_handler(commands=['blanket'])
def main(message):
    bot.send_message(message.chat.id, 'Мууррр, тепло')


@bot.message_handler(commands=['hobby'])
def main(message):
    bot.send_message(message.chat.id, 'Это моё любимое [видео](https://youtu.be/as2wtiau2ho?si=QlFoKYkPYMz_JU9L)',
                     parse_mode='Markdown')


bot.infinity_polling()