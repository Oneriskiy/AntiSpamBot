import aiogram
import asyncio
from aiogram import Bot, Router, Dispatcher, types
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from config import TOKEN, ADMIN_ID
dp = Dispatcher()
bot = Bot(TOKEN)
router = Router()
#выше нужные импорты

#декоратор для комманды старт - начальный декоратор
@router.message(Command("start"))
async def StartFunc(message: types.Message):
    await message.answer("Привет! Задай вопрос, интересующий тебя здесь\n\n Он обязательно дойдет нужному пользователю! ")

#Основной декоратор, для отправки сообщений
@router.message()
async def FirstFunc(message: types.Message):
    user_message = message.text
    await bot.send_message(ADMIN_ID,f"Сообщение от Пользователя {message.from_user.full_name} \nUsername = @ {message.from_user.username} \n\n{user_message}")
    await message.reply("Сообщение отправлено! Данный бот создан @Oneriiskiy")
  
     

async def main_func():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        # Запуск основной асинхронной функции
        asyncio.run(main_func())  # Запускаем все подготовительные шаги и бота
    except KeyboardInterrupt:
        print("Exit")