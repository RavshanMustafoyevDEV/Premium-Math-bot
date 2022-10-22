
from aiogram.types import CallbackQuery
from aiogram import types

from app import bot, dp, db, st, cfg
from keyboards import admin_mrk as adm

from aiogram.dispatcher import FSMContext



@dp.callback_query_handler(user_id=cfg.ADMINS,text="Ro'yxat📑")
async def list_mavzular(call:CallbackQuery, state:FSMContext):
    await call.message.delete()
    mavzular = db.get_mavzular()
    for val in mavzular:
        if val[2] == 0:
            narx = 'Bepul'

        else:
            narx = f"{val[2]} so'm"
        await bot.send_document(
            chat_id=call.message.chat.id, 
            document=val[4],
            reply_markup=adm.mainMenu,
            parse_mode='Markdown',
            caption=f"""
-----------------------------
ID: `{val[0]}` 🆔
Mavzu: *{val[1]}* 📑
Narxi: {narx} 💵

Mavzuda:
    ○
{val[3]}
    ○
-----------------------------
            """,
        )

    await call.message.answer(f"Mavzular soni : {len(mavzular)} ta 📚")









