from aiogram.types import CallbackQuery
from app import bot, dp, db, st
from app import mrk
from aiogram import types
from aiogram.dispatcher import FSMContext




@dp.message_handler(state=st.get_order, text='/cancel')
async def cancel_setNewMavzu(message, state:FSMContext):
    await state.finish()
    await message.answer("So'rov bekor qilindi ❌", reply_markup=mrk.mainMenu)


@dp.callback_query_handler(text="get_orderMavzu")
async def get_Buyurtma(call:CallbackQuery, state:FSMContext):
    await call.message.delete()
    await call.message.answer("Aktivlashtirilgan buyurtma kodingizni kiriting 🆔:", reply_markup=mrk.ReplyKeyboardRemove())
    await st.get_order.code.set()



@dp.message_handler(state=st.get_order.code)
async def hddjfb(message, state:FSMContext):
    await state.update_data(code=message.text)
    data = await state.get_data()
    code = data['code']

    result = db.get_reedem(code=code)
    if result:
        if result[1] == 'mavzu':
                if result[3] == True:
                    mv = db.get_mavzu(idMavzu=result[2])
                    for m in mv:
                        await message.answer_document(document=m[4], caption=f"""
ID : <strong>{m[0]}</strong> 🆔
Mavzu : <strong>{m[1]}</strong> 📑
Narxi : <strong>{m[2]}</strong> so'm 💵
Buyurtma kodingiz : <strong>{code}</strong> 🪪

Mavzu kursida :
    ○
{m[3]}
    ○

Xizmatimizdan foydalanganingiz uchun tashakkur 😊
                        """, reply_markup=mrk.mainMenu, parse_mode='html')
                        db.delete_reedem(reedem_code=code)
                        await message.answer("Ushbu buyurtma kodingizdan foydalanib bo'ldingiz ushbu kod ma'lumotlar omboridan o'chirildi❗")
                        await state.finish()

                else:
                    await message.answer("Sizni buyurtma kodingiz hali aktivlashtirilmagan ❗", reply_markup=mrk.mainMenu)
                    await state.reset_data()

        if result[1] == 'test':
            if result[3] == True:
                    test = db.get_test(idTest=result[2])
                    for m in test:
                        await message.answer_document(document=m[4], caption=f"""
ID : <strong>{m[0]}</strong> 🆔
Test mavzusi : <strong>{m[1]}</strong> 📑
Narxi : <strong>{m[3]}</strong> so'm 💵
Buyurtma kodingiz : <strong>{code}</strong> 🪪

Xizmatimizdan foydalanganingiz uchun tashakkur 😊
                        """, reply_markup=mrk.mainMenu, parse_mode='html')
                        db.delete_reedem(reedem_code=code)
                        db.set_saled_test(user_id=message.from_user.id, idTest=m[0], test_price=m[3])
                        await message.answer("Ushbu buyurtma kodingizdan foydalanib bo'ldingiz ushbu kod ma'lumotlar omboridan o'chirildi❗")
                        await state.finish()

            else:
                    await message.answer("Sizni buyurtma kodingiz hali aktivlashtirilmagan ❗", reply_markup=mrk.mainMenu)
                    await state.reset_data()



    else:
        await message.answer("Bunday buyurtma kodi mavjud emas❌", reply_markup=mrk.mainMenu)
        await state.reset_data()

    await state.finish()





