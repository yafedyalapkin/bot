# from aiogram import types, Bot
# from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor 
# import os 


# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton #Button - сама кнопка, Markup - клавиатура, в которую добавляются кнопки

# bot = Bot(token=os.getenv('TOKEN'))
# dp = Dispatcher(bot)







# urlknopka = InlineKeyboardButton(text='Заказать', url='https://broobro.ru/menu/#!/Pitstsa_30_sm/Pitstsa_30_sm_Tsyplenok_Teriyaki')
# urlklava = InlineKeyboardMarkup(row_width=1).add(urlknopka) #аргумент - ширина ряда (сколько кнопок поместится в ряд)



# @dp.message_handler(commands='ссылки')
# async def url_command(message : types.Message):
# 	await message.answer('Ссылочки:', reply_markup=urlk)















# executor.start_polling(dp, skip_updates=True)



# def register_handlers_client(dp : Dispatcher):
# 	dp.register_message_handler(url_command, commands=['ссылки'])