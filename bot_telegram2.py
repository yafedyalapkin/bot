from aiogram.utils import executor         #класс экзэкьютор нужен чтобы бот вышел в онлайн
from create_bot import dp                   
from data_base import sqlite_db



async def on_startup(_):             #при запуске бота...
    print('Бот вышел в онлайн')     
    sqlite_db.sql_start()            #запуск бд = модуль.функция()




from handlers import client, admin  #импортируем из папки хендлерс нужные нам файлы

client.register_handlers_client(dp) #регистрируем команды из клиенствой папки
admin.register_handlers_admin(dp)   #регистрируем команды из админской папки





executor.start_polling(dp, skip_updates=True, on_startup=on_startup)   #start_polling - запуск бота. dp - передаем диспетчер, 
                                                #skip_updates=True - чтобы когда бот вышел в онлайн пользователю не сыпались ответы 
                                                #от бота на запросы юзеров, пока он был офлайн
                                                #on_startup)


# from aiogram import Bot, types   #класс экзэкьютор нужен чтобы бот вышел в онлайн
# from aiogram.dispatcher import Dispatcher          #       
# from aiogram.utils import executor     #э

# import os

# bot = Bot(token=os.getenv('TOKEN'))
# dp = Dispatcher(bot)

# async def on_startup(_):             #при запуске бота...
#     print('Бот вышел в онлайн')     
    

# @dp.message_handler()
# async def echo_send(message):
#     await message.answer(message.text)

# executor.start_polling(dp, skip_updates=True, on_startup=on_startup)