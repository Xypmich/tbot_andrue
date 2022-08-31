import telebot
from telebot import types
import time


bot = telebot.TeleBot('5679848381:AAHbj5KokHqWEx-PKdgcryS--fzhE81gAZU')
owner_id = 375998759
# owner_id = 121471050


@bot.message_handler(commands=['start'])
def start(st_message):
    bot.send_message(st_message.chat.id, 'Здравствуйте!')
    time.sleep(0.5)
    anon_buttons(st_message)


def anon_buttons(ab_message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_1 = types.KeyboardButton('Анонимно')
    button_2 = types.KeyboardButton('Не анонимно')
    markup.add(button_1, button_2)
    msg = bot.send_message(ab_message.chat.id, 'Как хотите отправить историю?', reply_markup=markup)
    bot.register_next_step_handler(msg, story_message)


def story_message(s_message):
    if s_message.text == 'Анонимно':
        msg = bot.send_message(s_message.chat.id, 'Договорились! Присылайте свою историю.',
                               reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, if_anon)
    elif s_message.text == 'Не анонимно':
        msg = bot.send_message(s_message.chat.id, 'Договорились! Присылайте свою историю.',
                               reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, if_not_anon)
    else:
        error_msg = bot.send_message(s_message.chat.id, 'Не понимаю... Выберите один из вариантов.')
        bot.register_next_step_handler(error_msg, story_message)


def if_anon(a_message):
    bot.send_message(owner_id, f'Новая история!\n\n{a_message.text}')
    wakeup_bot(a_message)


def if_not_anon(na_message):
    bot.send_message(owner_id, f'Новая история!\n\n@{na_message.from_user.username}\n{na_message.text}')
    wakeup_bot(na_message)


def wakeup_bot(wu_message):
    new_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button = types.KeyboardButton('Прислать историю')
    new_markup.add(button)
    restart_msg = bot.send_message(wu_message.chat.id, 'Спасибо за вашу историю! Не стесняйтесь присылать ещё.',
                                   reply_markup=new_markup)
    bot.register_next_step_handler(restart_msg, anon_buttons)


bot.infinity_polling()
