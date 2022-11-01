from email import message
from aiogram.types import CallbackQuery
from app import bot, dp, db, st
from app import mrk
from aiogram import types
from aiogram.dispatcher import FSMContext




@dp.message_handler(state=st.get_order_mavzu, text='/cancel')
async def cancel_setNewMavzu(message, state:FSMContext):
    await state.finish()
    await message.answer("So'rov bekor qilindi ❌", reply_markup=mrk.mainMenu)


@dp.callback_query_handler(text="get_orderMavzu")
async def get_Buyurtma(call:CallbackQuery, state:FSMContext):
    await call.message.delete()
    await call.message.answer("Aktivlashtirilgan buyurtma kodingizni kiriting 🆔:", reply_markup=mrk.ReplyKeyboardRemove())
    await st.get_order_mavzu.code.set()



@dp.message_handler(state=st.get_order_mavzu.code)
async def hddjfb(message, state:FSMContext):
    await state.update_data(code=message.text)
    data = await state.get_data()
    code_mavzu = data['code']

    result = db.get_mavzu_reedem(code=code_mavzu)
    if result:
        for r in result:
            if r[3] == True:
                mv = db.get_mavzu(idMavzu=r[2])
                for m in mv:
                    await message.answer_document(document=m[4], caption=f"""
ID : <strong>{m[0]}</strong> 🆔
Mavzu : <strong>{m[1]}</strong> 📑
Narxi : <strong>{m[2]}</strong> so'm 💵
Buyurtma kodingiz : <strong>{code_mavzu}</strong> 🪪

Mavzu kursida :
    ○
{m[3]}
    ○

Xizatimizdan foydalanganingiz uchun tashakkur 😊
                    """, reply_markup=mrk.mainMenu, parse_mode='html')
                    db.delete_reedem(reedem_code=code_mavzu)
                    await message.answer("Ushbu buyurtma kodingizdan foydalanib bo'ldingiz ushbu kod ma'lumotlar omboridan o'chirildi❗")
                    await state.finish()

            else:
                await message.answer("Sizni buyurtma kodingiz hali aktivlashtirilmagan ❗", reply_markup=mrk.mainMenu)
                await state.reset_data()
    else:
        await message.answer("Bunday buyurtma kodi mavjud emas❌", reply_markup=mrk.mainMenu)
        await state.reset_data()

    await state.finish()





