from aiogram.types import CallbackQuery
from app import bot, dp, db, st
from app import mrk
from aiogram import types
from aiogram.dispatcher import FSMContext

@dp.message_handler(state=st.buyMavzu, text='/cancel')
async def cancel(message, state:FSMContext):
    await message.answer("Bekor qilindi❌", reply_markup=mrk.mainMenu)
    await state.reset_data()

@dp.callback_query_handler(text='buy_mavzu')
async def buy_mavzu(call:CallbackQuery, state:FSMContext):
    await call.message.delete()
    await call.message.answer("Sotib olayotgan mavzu ID sini kiriting:", reply_markup=mrk.ReplyKeyboardRemove())
    await st.buyMavzu.id.set()

@dp.message_handler(state=st.buyMavzu.id)
async def set_id_buyMavzu(message, state:FSMContext):
    if message.text.isdigit():
        await state.update_data(id=message.text)
        data = await state.get_data()
        result = db.buy_mavzu(type='mavzu', id_type=data['id'])
        

        if result:
            if result != 'free':
                await message.answer(f"""
Admin: <a href="t.me/Matematika_2_maktab" >Muhammadali Saydullayev</a> 👤
Karta raqam: <code>9860 1601 3541 9499</code> 💳
Buyurtma kodingiz: <code>{result}</code>

Kodni ko'chirib olish uchun kodni ustiga bosing 📑


Sizning buyurtmangiz muvaffaqiyatli yaratildi✅

Endi faqat uni aktivlashtirish qoldi xolos, kodni aktivlashtirish uchun:
1️⃣ Admin ga to'lov qilganingiz haqidagi kvitansiya yoki skrinshotni adminga jo'nating

2️⃣ Va buyurtma kodingizni ham adminga yuboring 👤

3️⃣ Admin kodingiz aktivlashgani haqida xabar bergandan so'ng <strong>Buyurtma</strong> > <strong>Buyurtmani olish</strong> bo'limiga buyurtma kodingizni kiriting va bot sizga buyurtma faylingizni yuboradi📩
                """, parse_mode='html', reply_markup=mrk.mainMenu)

            elif result == 'free':
                await message.answer(f"""
Bepul mavzularni <strong>Mavzu</strong> > <strong>Mavzuni qidirish</strong> bo'limiga ID sini yozsangiz bot sizga mavzu faylini yuboradi✅
""", parse_mode='html', reply_markup=mrk.mainMenu)
                await state.reset_data()

        else:
            await message.answer("Bunday ID dagi mavzu mavjud emas ❗", reply_markup=mrk.mainMenu)
            await state.finish()

    else:
        await message.answer("ID faqat raqamlardan iborat bo'lishi lozim❗")
        await st.buyMavzu.id.set()

    await state.finish()




