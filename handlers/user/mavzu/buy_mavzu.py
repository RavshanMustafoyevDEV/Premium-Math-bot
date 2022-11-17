from aiogram.types import CallbackQuery
from app import bot, dp, db, st
from app import mrk
from aiogram import types
from aiogram.dispatcher import FSMContext

@dp.message_handler(state=st.buyMavzu, text='/cancel')
async def cancel(message, state:FSMContext):
    await state.finish()
    await message.answer("Bekor qilindi❌", reply_markup=mrk.mainMenu)

@dp.callback_query_handler(text='buy_mavzu')
async def buy_mavzu(call:CallbackQuery, state:FSMContext):
    await call.message.delete()
    mavzular = db.get_premium_mavzular()
    mavzular2 = []

    for i,val in enumerate(mavzular, start=1):
        if int(val[2]) == 0:
            test = f'{i}) ID: `{val[0]}` | *{val[1]}* 🆓'
        else:
            test = f'{i}) ID: `{val[0]}` | *{val[1]}*'
        mavzular2.append(test)

    await call.message.answer('\n'.join(mavzular2), parse_mode='Markdown')    
    await call.message.answer("Sotib olayotgan mavzu ID sini kiriting:\nBekor qilish uchun - /cancel", reply_markup=mrk.ReplyKeyboardRemove())
    await st.buyMavzu.id.set()

@dp.message_handler(state=st.buyMavzu.id)
async def set_id_buyMavzu(message, state:FSMContext):
    if message.text.isdigit():
        await state.update_data(id=message.text)
        data = await state.get_data()
        result = db.buy_order(type='mavzu', id_type=data['id'])
        

        if result:
            if result != 'free':
                
                await message.answer(f"""
Sizning buyurtmangiz muvaffaqiyatli yaratildi✅

Endi faqat uni aktivlashtirish qoldi xolos, kodni aktivlashtirishni <a href="https://telegra.ph/Buyurtma-kodi-qanday-aktivlashtiriladi-11-08" ><strong>Qo'llanma</strong></a> dan bilib olsangiz bo'ladi

Admin: <a href="t.me/Matematika_2_maktab" >Muhammadali Saydullayev</a> 👤
Karta raqam: <code>9860 1601 3541 9499</code> 💳
Buyurtma kodingiz: <code><strong>{result}</strong></code>

Kodni ko'chirib olish uchun kodni ustiga bosing 📑
                """, parse_mode='html', reply_markup=mrk.mainMenu, disable_web_page_preview=True)
                
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




