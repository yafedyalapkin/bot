import sqlite3 as sq #импортируем модуль sqlite3 как sq (чтобы не писать все время sqlite3) для создание бд
from create_bot import bot, dp


#для инлайна
from aiogram import types, Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor 
import os 
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton




#функция для создания и запуска бд в файле боттг2
def sql_start():        
	global base, cur
	base = sq.connect('pizza_cool.db') #создаем бд. connect - подключить или создать
	cur = base.cursor()                 #класс cur. cursor нужен чтобы вносить изменения и читать данные 
	if base:                            
		print('Data Base connected OK!')  #когда бот вышел в онлайн принтуем эту фразу


	base.execute('CREATE TABLE IF NOT EXISTS sm30 (img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT, url TEXT)')   #создаем таблицу menu
	base.commit()   #сохраняет изменения в нашей бд


	base.execute('CREATE TABLE IF NOT EXISTS sm25 (img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT, url TEXT)')   #создаем таблицу menu
	base.commit()   #сохраняет изменения в нашей бд









#функция для внесения пицц через админку 30см
async def sql_add_pizza30(state):   
	async with state.proxy() as data:
		cur.execute('INSERT INTO sm30 VALUES (?, ?, ?, ?, ?)', tuple(data.values()))  #чтобы внести значения в таблицу
		base.commit() #сохраняет изменения в нашей бд


#функция для отображения меню в клиенской части
async def sql_read_pizza30(message):      
	for ret in cur.execute('SELECT * FROM sm30').fetchall():  #SELECT * - получить все. fetchall - получить все значения
		await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nСостав: {ret[2]}\n{ret[-2]} ₽')
		await bot.send_message(message.from_user.id, text='Хотите заказать?', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Да', url=f'{ret[-1]}')))









#функция для внесения пицц через админку 25см
async def sql_add_pizza25(state):   
	async with state.proxy() as data:
		cur.execute('INSERT INTO sm25 VALUES (?, ?, ?, ?, ?)', tuple(data.values()))  #чтобы внести значения в таблицу
		base.commit() #сохраняет изменения в нашей бд



#функция для отображения меню в клиенской части
async def sql_read_pizza25(message):
	for ret in cur.execute('SELECT * FROM sm25').fetchall():  #SELECT * - получить все. fetchall - получить все значения
		await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nСостав: {ret[2]}\n{ret[-2]} ₽')
		await bot.send_message(message.from_user.id, text='Хотите заказать?', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Да', url=f'{ret[-1]}')))








#функция для чтения всех пицц в админке (чтобы их можно было удалить)
async def sql_read2():
	return cur.execute('SELECT * FROM sm30').fetchall() #берем все значения из меню

#функция для удаления пиццы тоже через админку
async def sql_delete_command(data): #data - название пиццы
	cur.execute('DELETE FROM sm30 WHERE name == ?', (data,))   #посылаем эскьюэль запрос для удаления по названию какой-нибудь пиццы
	base.commit()   #сохраняет изменения в нашей бд





		




