import logging
from fireB import sM as send
from fireB import pusher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, executor, types
logging.basicConfig(level=logging.INFO)
TOKEN = '5015409457:AAFqbCRvLxRJJG17M0loUMKaVkGnHN94EL8'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def starts(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Грустные цитати")
    btn2 = types.KeyboardButton("Смешные цитати")
    btn3 = types.KeyboardButton("Цитаты про любовь")
    btn4 = types.KeyboardButton("Жизненые цитаты")
    btn5 = types.KeyboardButton("Умные цитаты")
    btn6 = types.KeyboardButton("Матевируешие цитаты")
    btn7 = types.KeyboardButton("Мысли о жизни")
    btn8 = types.KeyboardButton("Мудрые цитаты")

    markup.add(btn1)
    await bot.send_message(message.chat.id, "Привет.Выберите цытату ", reply_markup=markup)
    markup.add(btn2)
    await bot.send_message(message.chat.id, "Привет.Выберите цытату ", reply_markup=markup)
# try:
#     @dp.message_handler(text=['Грустные цитати'])
#     async def sM(message):
#         await message.reply(str(send('grustniy')))
#     @dp.message_handler(text=['Смешные цитати'])
#     async def sM(message):
#         await message.reply(str(send('smeshnye')))
#     @dp.message_handler(text=['Цитаты про любовь'])
#     async def sM(message):
#         await message.reply(str(send('grustniy')))
#     @dp.message_handler(text=['Жизненые цитаты'])
#     async def sM(message):
#         await message.reply(str(send('zhiznennye')))
#     @dp.message_handler(text=['Умные цитаты'])
#     async def sM(message):
#         await message.reply(str(send('umnye')))
#     @dp.message_handler(text=['Матевируешие цитаты'])
#     async def sM(message):
#         await message.reply(str(send('motiviruyushhie')))
#     @dp.message_handler(text=['Мысли о жизни'])
#     async def sM(message):
#         await message.reply(str(send('mysli_o_zhizni')))
#     @dp.message_handler(text=['Мудрые цитаты'])
#     async def sM(message):
#         await message.reply(str(send('mudrye_citaty')))
# except:pusher()
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)