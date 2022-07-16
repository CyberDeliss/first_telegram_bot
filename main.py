from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import telegram_api_token

bot = Bot(token=telegram_api_token)
dp = Dispatcher(bot)


@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    text = "Привет это бот, который расскажет тебе про отключение воды на улице Асатиани, это Ганя если что пишет"
    sent_message = await bot.send_message(chat_id=chat_id, text=text)
    print(sent_message.to_python())


executor.start_polling(dp)
