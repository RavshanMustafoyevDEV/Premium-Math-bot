from aiogram.types import CallbackQuery
from app import bot, dp, db, st
from app import mrk
from aiogram import types
from aiogram.dispatcher import FSMContext




@dp.callback_query_handler(text = 'my_mavzular')
async def get_my_mavzu(call:CallbackQuery):
    result = db.get_my_mavzu(user_id=call.message.chat.id)
    if result:
        list = []
        for i,val in enumerate(result, start=1):
            price = int(val[2])
            row = f"{i}) <strong>{val[1]}</strong> 📑 | <em>{val[3]}</em> 📅 | {price:,} so'm 💵"
            list.append(row)
        
        about_row = f"Sotib olgan mavzularingiz soni : {len(result)} ta 📑\n\n"

        fin_list = '\n'.join(list)
        await call.message.edit_text(text=about_row + fin_list, reply_markup=mrk.myMavzuMenu, parse_mode='html')

    else:
        await call.answer("Siz hali birorta ham test sotib olmadingiz 🫤", show_alert=True)


@dp.callback_query_handler(text='back_mavzu_user')
async def back_mavzu_user(call:CallbackQuery):
    await call.message.edit_text("Bo'limlardan birini tanlang:", reply_markup=mrk.mavzularMenu)








