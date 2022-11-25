from aiogram import types, Dispatcher  #импортируем то, что будет использоваться в коде
from create_bot import dp, bot 
from keyboards import kb_client
from aiogram.types import ReplyKeyboardMarkup  #удаляет клавиатуру после опрееленного действия (не понадобился пока)
from data_base import sqlite_db



# @dp.message_handler(commands=['start'])               #декоратор обозночает событие когда боту пишут /start. обработчик сообщений
async def commands_start(message : types.Message):    #асинхронная функция - многопоточная. Сюда попадают смс от юзеров
	await message.answer('Привет! Выбирай пиццу', reply_markup=kb_client)    #await - ждать. бот ждет смс.отвечает... 2арг - отвечает кнопками из другого файла






# @dp.message_handler(lambda message: message.text == 'Пиццы 30 см')
async def sm30(message : types.Message):
	await sqlite_db.sql_read_pizza30(message)


# @dp.message_handler(lambda message: message.text == 'Пиццы 25 см')
async def sm25(message : types.Message):
	await message.answer('Выбирай')  
	await sqlite_db.sql_read_pizza25(message)



# # @dp.message_handler(lambda message: message.text == 'Пиццы 20 см')
# async def sm20(message : types.Message):
# 	await message.answer('Выбирай')  



# @dp.message_handler() #если юзер пишет что-то другое (пустое смс)
# async def empty_msg(message : types.Message):
	# await message.answer('Выбирай из предложенного меню', reply_markup=kb_client)
	



def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(commands_start, commands=['start'])	

	dp.register_message_handler(sm30, lambda message: message.text == 'Пиццы 30 см') 
	dp.register_message_handler(sm25, lambda message: message.text == 'Пиццы 25 см')
	# dp.register_message_handler(sm20, lambda message: message.text == 'Меню')
	# dp.register_message_handler(empty_msg)









