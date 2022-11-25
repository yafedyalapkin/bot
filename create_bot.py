from aiogram import Bot                    #from - из. #импортируем класс бота, 
from aiogram.dispatcher import Dispatcher  #импортируем класс диспетчер #благодарся этому классу бот улавливает события и реагирует
import os                                  #os - модуль. импортируем чтобы прочитать наш токен из переменной среды окружения
from aiogram.contrib.fsm_storage.memory import MemoryStorage #MemoryStorage позволяет хранить данные в оперативке (для админики)

storage=MemoryStorage() #заускаем класс MemoryStorage #Создаем хранилище в оперативной памяти для машины состояний (для админики)

 
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage) #storage=storage - передаем экземпляр MemoryStorage