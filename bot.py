import telebot
import constants
from keyboards import location_keyboard
from candidate import Candidate


bot = telebot.TeleBot(constants.TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    bot.send_message(user_id, constants.hello_text, parse_mode='Markdown', reply_markup=location_keyboard)

    bot.send_message(57737851, f'\u2B50\uFE0F *Новый пользователь* — '
                               f'[{first_name}](tg://user?id={user_id}) ({user_id})', parse_mode='Markdown')


@bot.message_handler(commands=['help'])
def send_program(message):
    bot.send_message(message.from_user.id, constants.help_text, parse_mode='Markdown')


@bot.message_handler(commands=['abbreviations'])
def send_abbreviations(message):
    bot.send_message(message.from_user.id, constants.abbreviations, parse_mode='Markdown')


@bot.message_handler(commands=['memo'])
def send_memo(message):
    bot.send_photo(message.from_user.id, constants.memo_photo, caption=constants.memo_text, parse_mode='Markdown')


@bot.message_handler(commands=['program'])
def send_program(message):
    bot.send_message(message.from_user.id, constants.program, parse_mode='Markdown')


@bot.message_handler(content_types=['text'])
def text_message(message):
    user_id = message.from_user.id
    text = message.text

    bot.send_message(user_id, Candidate.get_my_candidate(address=text), parse_mode='Markdown',
                     reply_markup=location_keyboard)


@bot.message_handler(content_types=['location'])
def location_message(message):
    user_id = message.from_user.id
    location = (message.location.longitude, message.location.latitude)

    bot.send_message(user_id, Candidate.get_my_candidate(location=location), parse_mode='Markdown',
                     reply_markup=location_keyboard)



bot.polling()
