from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from randomWord import getRandomWord, words
from jokes import jokes, getRandomJoke

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def start_bot(_):
    print('Бот запущен')

# @dp.message_handler(commands=['start'])
# async def process_start_command(message: types.Message):
#     await bot.send_message(msg.from_user.id, 'Бот запущен')



@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\n/help чтобы узнать что я могу")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Вот что я пока что умею:\n/randomWord - назову какое-нибудь животное"
                        "\n/joke - расскажу шутку\n/guessInt - загадаю тебе число, а ты попрробуешь"
                        " отгадать\nИ не смей называть меня пидором!!!")

@dp.message_handler(commands=['randomWord'])
async def process_random_word_command(message: types.Message):
    await message.reply(getRandomWord(words))

@dp.message_handler(commands=['joke'])
async def process_random_joke_command(message: types.Message):
    await message.reply(getRandomJoke(jokes))


@dp.message_handler(commands=['guessInt'])
async def process_guess_int_command(message: types.Message):
    await message.reply('Ладно, этого пока не умею')


@dp.message_handler(content_types="text")
async def echo_message(msg: types.Message):
    if (msg.text == 'пидор') or (msg.text == 'ты пидор'):
        await msg.reply('ты чё, охуел?')
        await bot.send_message(msg.from_user.id, 'сам ты пидор')


@dp.message_handler(content_types="text")
async def echo_message(msg: types.Message):
    if msg.text == 'урод':
        await msg.reply('ты чё, охуел?')
        await bot.send_message(msg.from_user.id, 'сам ты пидор')


@dp.message_handler(content_types="text")
async def echo_message1(msg: types.Message):
    if (msg.text == 'игра') or (msg.text == 'Игра'):
        await msg.reply(getRandomWord(words))




# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=start_bot)