from aiogram.types import CallbackQuery
from app import bot, dp, db, st
from app import mrk
from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(text='my_tests_user')
async def sdbcasddhergegjcbds(call:CallbackQuery):
    user_id = call.message.chat.id
    res = db.get_my_tests(user_id=user_id)
    if res:
        list = []
        for i,val in enumerate(res, start=1):
            price = int(val[2])
            row = f"{i}) ID: <code>{val[0]}</code> | <em>{val[1]}</em> | {price:,} so'm"
            list.append(row)
        
        about_row = f"Sotib olgan testlaringiz soni : {len(res)} ta 📑\n\n"

        fin_list = '\n'.join(list)
        await call.message.edit_text(text=about_row + fin_list, reply_markup=mrk.my_testsMenu, parse_mode='html')
    
    else:
        await call.answer("Siz hali birorta ham test sotib olmadingiz 🫤", show_alert=True)













