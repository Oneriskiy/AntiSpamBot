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
    if (user_message != "Я не бот"):
        builder = InlineKeyboardMarkup(inline_keyboard=[    
                [InlineKeyboardButton(text="Узнать кто пишет", callback_data="answer")],
            ])
        await bot.send_message(ADMIN_ID,f"Сообщение от Пользователя {message.from_user.full_name} \n\n{user_message}", reply_markup = builder)
        await message.reply("Сообщение отправлено! Данный бот создан @Oneriiskiy")
    else:  
        await message.answer(f"{message.from_user.full_name} - Вы Бот")
     
@router.message()
async def FirstFunc(message: types.Message):
    user_message = message.text

    # Сохраняем user_id в callback_data
    builder = InlineKeyboardMarkup(inline_keyboard=[    
        [InlineKeyboardButton(text="Ответить", callback_data=str(message.from_user.id))],
    ])
    
    await bot.send_message(ADMIN_ID, f"Сообщение от Пользователя {message.from_user.full_name} \n\n{user_message}", reply_markup=builder)
    await message.reply("Сообщение отправлено! Данный бот создан @Oneriiskiy")

@router.callback_query()
async def answer(callback_query: types.CallbackQuery):
    user_id = int(callback_query.data.split('_')[1])
    user = await bot.get_chat(user_id)  
    await callback_query.message.edit_text(f"Имя пользователя: @{user.username} - Его имя: {user.full_name}")


async def main_func():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        # Запуск основной асинхронной функции
        asyncio.run(main_func())  # Запускаем все подготовительные шаги и бота
    except KeyboardInterrupt:
        print("Exit")