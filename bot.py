import telebot
import config


from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/hi.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("$ USD → BLR")
    item2 = types.KeyboardButton("€ EUR→ BLR")
    item3 = types.KeyboardButton("BLR → $ USD")
    item4 = types.KeyboardButton("BLR →€ EUR")

    markup.add(item1, item2, item3, item4)
    msg = bot.send_message(message.chat.id, "Выберите вариант перевода. Курсы валют актуальны на сегодня по MyFin", reply_markup=markup)
    bot.register_next_step_handler(msg, proccess_coin_step)


@bot.message_handler(content_types=['text'])
def proccess_coin_step(message):
    if message.chat.type == 'private':
        if message.text == "$ USD → BLR":
            msg = bot.send_message(message.chat.id, "введите сумму для перевода")
            bot.register_next_step_handler(msg, usdblr)
        elif message.text == "€ EUR→ BLR":
            msg = bot.send_message(message.chat.id, "введите сумму для перевода")
            bot.register_next_step_handler(msg, euroblr)
        elif message.text == "BLR → $ USD":
            msg = bot.send_message(message.chat.id, "введите сумму для перевода")
            bot.register_next_step_handler(msg, blreuro)
        elif message.text == "BLR →€ EUR":
            msg = bot.send_message(message.chat.id, "введите сумму для перевода")
            bot.register_next_step_handler(msg, blreuro)

# перевод долларов в рубли
def usdblr(message):
    try:
       bot.send_message(message.chat.id, float(message.text) * float(config.usd))
    except ValueError:
        bot.send_message(message.chat.id, "введите число")

# перевод евро в рубли
def euroblr(message):
    try:
        bot.send_message(message.chat.id, float(message.text) * float(config.eur))
    except ValueError:
        bot.send_message(message.chat.id, "введите число")

# перевод рублей в доллары
def blrusd(message):
    try:
        bot.send_message(message.chat.id, float(message.text) / float(config.usd))
    except ValueError:
        bot.send_message(message.chat.id, "введите число")

# перевод рублей в евро
def blreuro(message):
    try:
        bot.send_message(message.chat.id, float(message.text) / float(config.eur))
    except ValueError:
        bot.send_message(message.chat.id, "введите число")


bot.polling(none_stop=True)