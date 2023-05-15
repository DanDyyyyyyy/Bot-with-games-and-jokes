from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup\InlineKeyboardMarkup, InlineKeyboardButton

keyboards = [
    [types.KeyboardButton(text='randomWord')],
    {types.KeyboardButton(text='joke')},
    [types.KeyboardButton(text='guessInt')]
]
keyboard = types.ReplyKeyboardMarkup(keyboard=keyboards)



button_hi = KeyboardButton('Привет! 👋')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)