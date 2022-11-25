from aiogram.types import ReplyKeyboardMarkup, KeyboardButton #, ReplyKeyboardRemove

b1 = KeyboardButton('Пиццы 30 см')
b2 = KeyboardButton('Пиццы 25 см')
# b3 = KeyboardButton('Меню')




kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).add(b1).insert(b2)#.add(b3)  #1арг - уменьшить кнопки, 2арг - после нажатия на кнопку, клавиатура исчезает



