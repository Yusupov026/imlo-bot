import logging

from aiogram import Bot, Dispatcher, executor, types
from checkWord import checkWord

API_TOKEN = '5982793774:AAFeQFgIUoK2dbMCSwcndnbavoLMhkFLKyw'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Welcome to Imlo_bot ")



@dp.message_handler(commands='help')
async def hel_user(message: types.Message):
    await message.answer("Botdan foydalanish uchun so'z yuboring.")


@dp.message_handler()
async def checkImlo(message: types.Message):
    word = message.text
    result = checkWord(word)
    if result['available']:
        response = f"✔ {word.capitalize()}"
    else:
        response = f"✖{word.capitalize()}\n"
        for text in result['matches']:
            response += f"✔ {text.capitalize()}\n"
    await message.answer(response)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)