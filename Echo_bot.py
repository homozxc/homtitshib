from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
API_TOKEN: str = '6079849603:AAFz_b28AGFZ7lLBi0Anw5DHh4_HBOMVWo4'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе твое сообщение')


# Этот хэндлер будет срабатывать на отправку боту фото
# @dp.message()
# async def send_photo_echo(message: Message):
#     await message.reply_photo(message.audio.file_id)
#
# @dp.message()
# async def send_video_echo(message: Message):
#     await message.reply_video(message.video.file_id)
#
# @dp.message()
# async def send_stiker_echo(message: Message):
#     await message.reply_sticker(message.sticker.file_id)
#
# @dp.message()
# async def send_audio_echo(message: Message):
#     await message.reply_audio(message.photo[0].file_id)
#
#
# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)

if __name__ == '__main__':
    dp.run_polling(bot)