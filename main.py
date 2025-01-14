import aiogram
import asyncio
from aiogram import Bot, Router, Dispatcher, types
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from config import TOKEN, ADMIN_ID
dp = Dispatcher()
bot = Bot(TOKEN)
router = Router()

@router.message(Command("start"))
async def StartFunc(message: types.Message):
    await message.answer("Привет! Задай вопрос, интересующий тебя здесь\n\n Он обязательно дойдет нужному пользователю! ")

@router.message()
async def FirstFunc(message: types.Message):
    user_message = message.text
    if (user_message != "Я бот"):
        builder = InlineKeyboardMarkup(inline_keyboard=[    
                [InlineKeyboardButton(text="Узнать кто пишет", callback_data="answer")],
            ])
        await bot.send_message(ADMIN_ID,f"Сообщение от Пользователя {message.from_user.full_name} \n\n{user_message}", reply_markup = builder)
        await message.reply("Сообщение отправлено! Данный бот создан @Oneriiskiy")
    else:  
        await message.answer(f"{message.from_user.full_name} - Вы Бот")
     

@router.callback_query(lambda c: c.data == 'answer')
async def answer(callback_query: types.CallbackQuery):
    username = callback_query.from_user.username  
    fullname = callback_query.from_user.full_name  
    await callback_query.message.edit_text(f"Имя пользователя: @{username} - Его имя - {fullname}")


async def main_func():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        # Запуск основной асинхронной функции
        asyncio.run(main_func())  # Запускаем все подготовительные шаги и бота
    except KeyboardInterrupt:
        print("Exit")