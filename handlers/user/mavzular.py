
from aiogram.types import CallbackQuery
from app import bot, dp, db, st
from app import mrk
from aiogram import types
from aiogram.dispatcher import FSMContext



@dp.message_handler(text="Mavzular📃")
async def start_command(message):
    await message.answer(message.text, reply_markup=mrk.ReplyKeyboardRemove())
    await message.answer("Bo'limlardan birini tanlang:", reply_markup=mrk.mavzularMenu)











@dp.callback_query_handler(text="list_mavzular")
async def list_mavzular(call:CallbackQuery, state:FSMContext):
    await call.message.delete()
    mavzular = db.get_mavzular()
    mavzular2 = []

    for i,val in enumerate(mavzular, start=1):
        if int(val[2]) == 0:
            test = f'{i}) ID: `{val[0]}` | *{val[1]}* 🆓'
        else:
            test = f'{i}) ID: `{val[0]}` | *{val[1]}*'
        mavzular2.append(test)

    await call.message.answer('\n'.join(mavzular2), parse_mode='Markdown')    
    await call.message.answer(f"""
Mavzular soni : {len(mavzular)} ta 📚

Bepul mavzularni <strong>Mavzu</strong> > <strong>Mavzuni qidirish</strong> bo'limiga ID sini yozsangiz bot sizga mavzu faylini yuboradi✅

""", parse_mode='html', reply_markup=mrk.mainMenu)







