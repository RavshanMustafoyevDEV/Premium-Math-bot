
from aiogram.types import CallbackQuery
from app import bot, dp, db, st
from app import mrk
from aiogram import types
from aiogram.dispatcher import FSMContext



@dp.message_handler(text="Mavzular📃")
async def start_command(message:types.Message):
    await message.answer(message.text, reply_markup=mrk.ReplyKeyboardRemove())
    await message.answer("Bo'limlardan birini tanlang:", reply_markup=mrk.mavzularMenu)


@dp.callback_query_handler(text="list_mavzular")
async def list_mavzular(call: CallbackQuery):
    await call.message.edit_text("Tanlang:", reply_markup=mrk.mavzu_typeMenu)



@dp.callback_query_handler(text='get_free_mavzular')
async def list_m(call:CallbackQuery, state:FSMContext):
    back_mavzular = mrk.InlineKeyboardMarkup().add(
        mrk.InlineKeyboardButton("Orqaga🔙", callback_data='back_mavzular')
    )
    mavzular = db.get_free_mavzular()
    mavzular2 = []

    for i,val in enumerate(mavzular, start=1):
        if int(val[2]) == 0:
            test = f'{i}) ID: <code>{val[0]}</code> | <strong>{val[1]}</strong> 🆓'
        else:
            test = f'{i}) ID: <code>{val[0]}</code> | <strong>{val[1]}</strong>'
        mavzular2.append(test)

    fin_list = '\n'.join(mavzular2)

    await call.message.edit_text(f"""
Mavzular soni : {len(mavzular)} ta 📚

Bepul mavzularni <strong>Mavzu</strong> > <strong>Mavzuni qidirish</strong> bo'limiga ID sini yozsangiz bot sizga mavzu faylini yuboradi✅

Ro'yxat:
{fin_list}
    """, parse_mode='html', reply_markup=back_mavzular)    
    


@dp.callback_query_handler(text='get_premium_mavzular')
async def list_m(call:CallbackQuery, state:FSMContext):
    back_mavzular = mrk.InlineKeyboardMarkup().add(
        mrk.InlineKeyboardButton("Orqaga🔙", callback_data='back_mavzular')
    )
    mavzular = db.get_premium_mavzular()
    mavzular2 = []

    for i,val in enumerate(mavzular, start=1):
        if int(val[2]) == 0:
            test = f'{i}) ID: `{val[0]}` | *{val[1]}* 🆓'
        else:
            test = f'{i}) ID: `{val[0]}` | *{val[1]}*'
        mavzular2.append(test)

    fin_list = '\n'.join(mavzular2)

    await call.message.edit_text(text=f"Mavzular soni: *{len(mavzular)}*\n\n{fin_list}", parse_mode='markdown', reply_markup=back_mavzular)    
    


@dp.callback_query_handler(text='back_mavzular')
async def back_m(call:CallbackQuery):
    await call.message.edit_text("Tanlang:", reply_markup=mrk.mavzularMenu)

