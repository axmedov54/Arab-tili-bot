from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo,InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder






menyu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Arab Harflari"), KeyboardButton(text="Arab Harflari O`qilish")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


oqish = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="ا alif"), KeyboardButton(text="ب ba"), KeyboardButton(text="ت ta")],
        [KeyboardButton(text="ث fa"), KeyboardButton(text="ج jim"), KeyboardButton(text="ح ha")],
        [KeyboardButton(text="خ xo"), KeyboardButton(text="د dal"), KeyboardButton(text="ذ zal")],
        [KeyboardButton(text="ر ro"), KeyboardButton(text="ز za"), KeyboardButton(text="س sin")],
        [KeyboardButton(text="ش shin"), KeyboardButton(text="ص sod"), KeyboardButton(text="ض dod")],
        [KeyboardButton(text="ط to"), KeyboardButton(text="ظ za"), KeyboardButton(text="ع ayn")],
        [KeyboardButton(text="غ g'ayn"), KeyboardButton(text="ف fa"), KeyboardButton(text="ق qof")],
        [KeyboardButton(text="ك kaf"), KeyboardButton(text="ل lam"), KeyboardButton(text="م mim")],
        [KeyboardButton(text="ن nun"), KeyboardButton(text="ه ha"), KeyboardButton(text="و vov")],
        [KeyboardButton(text="ي ya")],[KeyboardButton(text="Ortga <-")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

