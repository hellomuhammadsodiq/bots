import asyncio

from aiogram import Bot, Dispatcher, executor


bot = Bot(token="5294483643:AAEGdPBD_LaJiOIhy4G1goYtDqHPmiFVUgg")
bot_dispatcher = Dispatcher(bot=bot)


@bot_dispatcher.message_handler()
async def new_timer_message(message):
	try:
		timer_seconds = int(message.text)
	except (ValueError, TypeError):
		await bot.send_message(chat_id=message.chat.id, text="𝓢𝓪𝓵𝓸𝓶 𝓶𝓮𝓷 𝓽𝓲𝓶𝓮𝓻 𝓫𝓸𝓽 son kiriting:")
		return

	new_message  = await bot.send_message(chat_id=message.chat.id, text=f"Sizning taymeringiz bu yerda: {timer_seconds}")

	for seconds_left in range(timer_seconds -1, -1, -1):
		await asyncio.sleep(1)
		await new_message.edit_text(text=f"Sizning taymeringiz bu yerda: {seconds_left}")

	await bot.send_message(chat_id=message.chat.id, text=f"Sizning vaqtingiz tugadi".upper())


if __name__ == '__main__':
    executor.start_polling(dispatcher=bot_dispatcher)