import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup

from config import BOT_TOKEN as token,Kanal_id
from button import menyu,oqish
from aiogram.filters import Filter


bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

class CheksupChanel(Filter):
  async def __call__(self,message:Message,bot:Bot):
    user_ststus=await bot.get_chat_member(Kanal_id,message.from_user.id)
    if user_ststus.status in ['creator','administrator','member']:
      return False
    return True


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Assalomu Aleykum, {html.bold(message.from_user.full_name)}!", reply_markup=menyu)

@dp.message(CheksupChanel())
async def obuna1(message:Message):
  Kanal_link = 't.me/kino_bot_uz1'
  kanallar=InlineKeyboardMarkup(
   inline_keyboard=[
     [InlineKeyboardButton(text='OBUNA BOLING :)',url=Kanal_link)]
   ]
 )
  await message.answer_photo(photo='https://codecapsules.io/wp-content/uploads/2023/08/comparing-telegram-bot-hosting-providerspng.png',caption='Kanalga obuna boling',reply_markup=kanallar)

@dp.message()
async def xabar(message:Message):
  await message.answer('Xabar Saqlandi')
  await message.send_copy(chat_id=-1002164151558)
 

@dp.message(F.text=='Arab Harflari')
async def echo_handler(message: Message) -> None:
    await message.answer_photo(photo="https://t.me/arab_alifbosi_Tajvid_darslari/4",caption='Мазкур 28 ҳарфнинг барчаси ундош ҳарфлар ҳисобланиб, улар мабоний (ўзгармайдиган) ҳарфлар деб айтилади.', reply_markup=menyu)
    await message.answer_video(video="https://t.me/arab_tili_alifbosi/48", reply_markup=menyu)


@dp.message(F.text=='Arab Harflari O`qilish')
async def namoz2(message:Message):
  await message.answer(text='Arab alifbosi',reply_markup=oqish)    

@dp.message(F.text=='ا alif')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/49',reply_markup=oqish)    

@dp.message(F.text=='ب ba')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/56',reply_markup=oqish) 

@dp.message(F.text=='ت ta')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/53',reply_markup=oqish)   

@dp.message(F.text=='ث fa')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/65',reply_markup=oqish)   

@dp.message(F.text=='ج jim')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/68',reply_markup=oqish)   

@dp.message(F.text=='ح ha')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/70',reply_markup=oqish)   

@dp.message(F.text=='خ xo')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/69',reply_markup=oqish)   

@dp.message(F.text=='د dal')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/73',reply_markup=oqish)   

@dp.message(F.text=='ذ zal')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/75',reply_markup=oqish)   

@dp.message(F.text=='ر ro')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/50',reply_markup=oqish)   

@dp.message(F.text=='ز za')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/51',reply_markup=oqish)   

@dp.message(F.text=='س sin')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/64',reply_markup=oqish)   

@dp.message(F.text=='ش shin')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/63',reply_markup=oqish)   

@dp.message(F.text=='ص sod')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/66',reply_markup=oqish)   

@dp.message(F.text=='ض dod')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/74',reply_markup=oqish)   

@dp.message(F.text=='ط to')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/67',reply_markup=oqish)   

@dp.message(F.text=='ظ za')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/76',reply_markup=oqish)   

@dp.message(F.text=='ع ayn')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/72',reply_markup=oqish)   

@dp.message(F.text=='غ g`ayn')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/71',reply_markup=oqish)   

@dp.message(F.text=='ف fa')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/61',reply_markup=oqish)   

@dp.message(F.text=='ق qof')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/62',reply_markup=oqish)   

@dp.message(F.text=='ك kaf')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/57',reply_markup=oqish)   

@dp.message(F.text=='ل lam')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/58',reply_markup=oqish)   

@dp.message(F.text=='م mim')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/52',reply_markup=oqish)   

@dp.message(F.text=='ن nun')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/54',reply_markup=oqish)   

@dp.message(F.text=='ه ha')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/60',reply_markup=oqish)   

@dp.message(F.text=='و vov')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/59',reply_markup=oqish)   

@dp.message(F.text=='ي ya')
async def namoz2(message:Message):
  await message.answer_video(video='https://t.me/arab_tili_alifbosi/55',reply_markup=oqish)   


@dp.message(F.text=='Ortga <-')
async def namoz2(message:Message):
  await message.answe(text='Asosiy Menyu',reply_markup=menyu)   


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except:
        print("Tugadi")