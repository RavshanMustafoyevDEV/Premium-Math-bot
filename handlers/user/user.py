from aiogram.types import CallbackQuery
from app import bot, dp, db, st
from app import mrk

from aiogram.dispatcher import FSMContext


#start handler
@dp.message_handler(commands=['start'])
async def start_command(message):
    if db.checkUser(message.from_user.id):
        await message.answer(f"Salom {message.from_user.first_name}🖐️", reply_markup=mrk.mainMenu)    
    else:
        await message.answer(f"Salom, {message.from_user.first_name}.\nBotimizdan to'liq foydalanish uchun ro'yxatdan o'ting !", reply_markup=mrk.regMenu)



@dp.message_handler(content_types=['contact'])
async def registUser(message):
    number = message.contact.phone_number
    id = message.from_user.id
    name = message.from_user.full_name

    result = db.regUser(id, name, number)

    if result:
        await message.answer("Siz ro'yxatdan o'tdingiz, botdan to'laqonli foydalanishingiz mumkin", reply_markup=mrk.mainMenu)

    else:
        await message.answer("Siz avvaldan ro'yxatdan o'tgansiz )")


@dp.callback_query_handler(text="mainMenuUser")
async def mainMenuAdmin(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer("Bosh menyu🏠", reply_markup=mrk.mainMenu)


#Buyurtma menu
@dp.message_handler(text="Buyurtma📦")
async def get_order(message):
    await message.answer(message.text, reply_markup=mrk.ReplyKeyboardRemove())
    await message.answer("Bo'limni tanlang :", reply_markup=mrk.buyurtmaMenu)

