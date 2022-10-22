from aiogram.types import CallbackQuery
from app import bot, dp, db, st, cfg
from keyboards import admin_mrk as adm

from aiogram.dispatcher import FSMContext


#start handler
@dp.message_handler(commands=['admin'], user_id=cfg.ADMINS)
async def start_command(message):
    await message.answer('Admin Panel', reply_markup=adm.mainMenu)


@dp.callback_query_handler(text="mainMenu", user_id=cfg.ADMINS)
async def mainMenuAdmin(call:CallbackQuery):
    await call.message.answer("Bosh menyu🏠", reply_markup=adm.mainMenu)








