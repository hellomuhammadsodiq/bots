import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'YOUR TOKEN'
wikipedia.set_lang('uz')    

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """This handler will be called when user sends `/start` or `/help` command"""
    await message.reply("Wikipedia Botiga Xush Kelibsiz! 😊 Bu yerda o`zingiz istagan malumot topishingiz mumkin\n ")


@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        await message.reply("please wait...")
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Kechirasiz bunaqa maqola topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
