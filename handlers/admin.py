from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text

from data_base import sqlite_db
from keyboards import admin_kb               #импортируем из файла с кнопками, кнопки админа
from keyboards import client_kb  
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton  #для инлайн кнопки



ID = None

#Получаем айди текущего админа (модератора) для бота. для того чтобы доступ к админке был только у модера
# @dp.message_handlers(commands=['moderator'], is_chat_admin=True) 
async def make_changes_command(message: types.Message):
	global ID 
	ID = message.from_user.id 
	await bot.send_message(message.from_user.id, 'что ты хочешь?', reply_markup=admin_kb.button_case_admin)
	await message.delete()






class FSMAdmin(StatesGroup):  #идем по пунктам в админке с состояния фото до состояния прайса
	photo = State()
	name = State()
	description = State()
	price = State()

	url = State()







#0. Начало диалога с ботом для загурзки новой пиццы через админку
# @dp.message_handlers(commands='Загрузить', state=None)  #state=None потому бот пока еще не находится в машине состояний, после фото врубится
async def cm_start(message : types.Message):
	if message.from_user.id == ID:
		await FSMAdmin.photo.set()
		await message.reply('Загрузи фото')


#1. бот получает фото и записывает его в словарь
# @dp.message_handlers(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message : types.Message, state : FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:                    #сохраняем данные в дату
			data['photo'] = message.photo[0].file_id
		await FSMAdmin.next()
		await message.reply('Теперь введи название пиццы')


#2. бот получает название, теперь хочет получить описание
# @dp.message_handlers(state=FSMAdmin.name)
async def load_name(message : types.Message, state : FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['name'] = message.text
		await FSMAdmin.next()
		await message.reply('Введи описание')


#3. бот получает третий ответ
# @dp.message_handlers(state=FSMAdmin.description)
async def load_description(message : types.Message, state : FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['description'] = message.text
		await FSMAdmin.next()
		await message.reply('Теперь укажи цену')


#4. бот получает четвертый ответ и использует полученные данные
# @dp.message_handlers(state=FSMAdmin.price)
async def load_price(message : types.Message, state : FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['price'] = float(message.text)  #флоат для плавующей точки в цене
		await FSMAdmin.next()
		await message.reply('Кинь ссылку на заказ')



#5. url eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
# @dp.message_handlers(state=FSMAdmin.price)
async def load_url(message : types.Message, state : FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['url'] = message.text  




		await sqlite_db.sql_add_pizza25(state) #вносим пиццу с описанием в бд
		await message.answer('Готово!')

		await state.finish()
		await message.answer('Ещё?', reply_markup=admin_kb.button_case_admin)

		



#удаление пицц
@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):
	await sqlite_db.sql_delete_command(callback_query.data.replace('del ', ''))
	await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} удалена.', show_alert=True)

# @dp.message_handler(commands='Удалить')
async def delete_item(message: types.Message):
	if message.from_user.id == ID:
		read = await sqlite_db.sql_read2()
		for ret in read:
			await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nСостав: {ret[2]}\n{ret[-2]} ₽')
			await bot.send_message(message.from_user.id, text='м?', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'del {ret[1]}')))





#Выход из машины состояний
# @dp.message_handlers(state="*", commands='отмена')                        # * - означает любое из 4 состояний
# @dp.message_handlers(Text(equals='отмена', ignore_case=True), state="*")  #при вызове команды 'отмена', бот выводится из машины состояний
async def cancel_handler(message: types.Message, state: FSMContext):        #несмотря на то, в каком из 4 состоянии он был
	if message.from_user.id == ID:
		current_state = await state.get_state()
		if current_state is None:
			return
		await state.finish()   #бот выходит из машины состояния и очищает все что мы записали
		await message.reply('Ок. Давай заново', reply_markup=admin_kb.button_case_admin)





#Регистрируем все хендлеры в функцию деф чтобы импортировать их в основной файл
def register_handlers_admin(dp : Dispatcher):
	dp.register_message_handler(cm_start, lambda message: message.text == 'Загрузить', state=None)
	dp.register_message_handler(cancel_handler, state="*", commands='отмена')
	dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
	dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
	dp.register_message_handler(load_name, state=FSMAdmin.name)
	dp.register_message_handler(load_description, state=FSMAdmin.description)
	dp.register_message_handler(load_price, state=FSMAdmin.price)

	dp.register_message_handler(load_url, state=FSMAdmin.url)

	dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)
	# dp.register_message_handler(del_callback_run, lambda x: x.data and x.data.startswith('del '))
	dp.register_message_handler(delete_item, lambda message: message.text == 'Удалить', state=None)

