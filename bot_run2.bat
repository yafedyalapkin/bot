@echo off
rem #для того чтобы служебная инфа самого бат-файла постоянно не спамила нам в консоли


call C:\Telegram_bot2\venv\Scripts\activate   
rem #call - вызов вирт. окр. 


cd C:\Telegram_bot2     
rem #cd - переход по папкам командной строки  #залазим внутырь папки


set TOKEN=5784471611:AAGRbrugLIQyjmfpLi2anun-kIKyx8Ahlw4
rem #set - переменная среды окружения #TOKEN - имя переменной #set - множество уникальных элементов


python bot_telegram2.py   
rem #файл, который нам надо запустить 


pause   
rem если в скрипте возникнет ошибка, окно консоли закроется и мы ошибку не увидим


