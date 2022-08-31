import telebot


bot = telebot.TeleBot('5679848381:AAHbj5KokHqWEx-PKdgcryS--fzhE81gAZU')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Пришлите свою историю и мы её опубликуем анонимно!')


@bot.message_handler(content_types=['text'])
def story_message(message):
    bot.send_message(121471050, f'Новая история!\n\n{message.from_user.username}\n{message.text}')
    bot.send_message(message.chat.id, 'Спасибо за вашу историю! Не стесняйтесь присылать ещё.')


bot.infinity_polling()
