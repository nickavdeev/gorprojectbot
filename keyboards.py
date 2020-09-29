from telebot import types


location_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)
location_keyboard.add(types.KeyboardButton(text='\U0001F5FA Отправить геопозицию', request_location=True))
