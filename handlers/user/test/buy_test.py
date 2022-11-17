from aiogram.types import CallbackQuery
from app import bot, dp, db, st
from app import mrk
from aiogram import types
from aiogram.dispatcher import FSMContext

@dp.message_handler(text='/cancel', state=st.buyTest)
async def canc_buy_test(message:types.Message, state:FSMContext):
    await state.finish()
    await message.answer("Bekor qilindi❌", reply_markup=mrk.mainMenu)

@dp.message_handler(text='/cancel', state=st.get_free_test)
async def canc_buy_test(message:types.Message, state:FSMContext):
    await state.finish()
    await message.answer("Bekor qilindi❌", reply_markup=mrk.mainMenu)




# Premium testlar
@dp.callback_query_handler(text='pre_tests')
async def start_buy_test(call:CallbackQuery, state:FSMContext):
    units_menu = mrk.InlineKeyboardMarkup(row_width=2)
    for i in db.list_unit():
        units_menu.insert(
            mrk.InlineKeyboardButton(text=i[0], callback_data=i[0]),
        )
    
    await call.message.edit_text("Qaysi mavzu bo'yicha test xarid qilmoqchisiz ?", reply_markup=units_menu)
    await st.buyTest.unit.set()



@dp.callback_query_handler(state=st.buyTest.unit)
async def sdjbsvdj(call:CallbackQuery, state:FSMContext):
    await state.update_data(unit=call.data)
    dt = await state.get_data()
    test = db.get_random_test_by_unit(unit=dt['unit'], not_test_id=0)
    if test:  
        await call.message.delete()
        await state.update_data(test_id=test[0])
        
        await call.message.answer(f"""
Test ID : {test[0]} 🆔
Test mavzusi : {test[1]} 📑
Test savollari soni : {len(test[2])} ta ❓ 
Test narxi : {test[3]} so'm 🪙

Ushbu testni sotib olasizmi ?
        """, reply_markup=mrk.okMenu)

        await st.buyTest.ok.set()

    else:
        await call.message.delete()
        await call.message.answer("Bu mavzu bo'yicha hozircha testlar mavjud emas (", reply_markup=mrk.mainMenu)
        await state.finish()


@dp.callback_query_handler(state=st.buyTest.ok)
async def jdnvsdvvcjs(call:CallbackQuery, state:FSMContext):
    await state.update_data(ok = call.data)
    dt = await state.get_data()

    if dt['ok'] == 'yes':
        await call.message.delete()
        result = db.buy_order(type='test', id_type=dt['test_id'])
        await call.message.answer(f"""
Sizning buyurtmangiz muvaffaqiyatli yaratildi✅

Endi faqat uni aktivlashtirish qoldi xolos, kodni aktivlashtirishni <a href="https://telegra.ph/Buyurtma-kodi-qanday-aktivlashtiriladi-11-08" ><strong>Qo'llanma</strong></a> dan bilib olsangiz bo'ladi

Admin: <a href="t.me/Matematika_2_maktab" >Muhammadali Saydullayev</a> 👤
Karta raqam: <code>9860 1601 3541 9499</code> 💳

Buyurtma kodingiz: <code><strong>{result}</strong></code>

Kodni ko'chirib olish uchun kodni ustiga bosing 📑
                """, parse_mode='html', reply_markup=mrk.mainMenu, disable_web_page_preview=True)
        await state.finish()


    elif dt['ok'] == 'no':
        await state.finish()
        await call.answer("Bekor qilindi❌", show_alert=True)
        await call.message.edit_text("Bo'limlardan birini tanlang:", reply_markup=mrk.testMenu)


    elif dt['ok'] == 'other_test':
        test = db.get_random_test_by_unit(unit=dt['unit'], not_test_id=dt['test_id'])
        try:
            await state.update_data(test_id=test[0])

            await call.message.edit_text(f"""
Test ID : {test[0]} 🆔
Test mavzusi : {test[1]} 📑
Test savollari soni : {len(test[2])} ta ❓ 
Test narxi : {test[3]} so'm 🪙

Ushbu testni sotib olasizmi ?
                """, reply_markup=mrk.okMenu)
            await st.buyTest.ok.set()

        except:
            await call.answer("Ushbu mavzu bo'yicha faqat shu test mavjud (")
            await st.buyTest.ok.set()
        




@dp.callback_query_handler(text='free_tests')
async def hjbcsdhjbvbs(call:CallbackQuery, state:FSMContext):
    units_menu = mrk.InlineKeyboardMarkup(row_width=2)
    for i in db.list_unit():
        units_menu.insert(
            mrk.InlineKeyboardButton(text=i[0], callback_data=i[0]),
        )
    
    await call.message.edit_text("Qaysi mavzu bo'yicha test xarid qilmoqchisiz ?", reply_markup=units_menu)
    await st.get_free_test.unit.set()

@dp.callback_query_handler(state=st.get_free_test.unit)
async def hgdshsd(call:CallbackQuery, state:FSMContext):
    await state.update_data(unit=call.data)
    dt = await state.get_data()
    test = db.get_random_free_test_by_unit(unit=dt['unit'], not_test_id=0)

    if test:  
        await call.message.delete()
        await state.update_data(test_id=test[0])
        
        await call.message.answer(f"""
Test ID : {test[0]} 🆔
Test mavzusi : {test[1]} 📑
Test javoblari : {test[2].upper()} ({len(test[2])} ta savol) ❓ 
Test narxi : Bepul 🪙

Ushbu testni olasizmi (Bepul) ?
        """, reply_markup=mrk.okMenu)

        await st.get_free_test.ok.set()

    else:
        await call.message.delete()
        await call.message.answer("Bu mavzu bo'yicha hozircha testlar mavjud emas (", reply_markup=mrk.mainMenu)
        await state.finish()




@dp.callback_query_handler(state=st.get_free_test.ok)
async def ahsbchjabschj(call:CallbackQuery, state:FSMContext):
    await state.update_data(ok = call.data)
    dt = await state.get_data()

    if dt['ok'] == 'yes':
        await call.message.delete()
        fin_test1 = db.get_test(idTest=dt['test_id'])
        for fin_test in fin_test1:
            await call.message.answer_document(caption=f"""
Test ID : {fin_test[0]} 🆔
Test mavzusi : {fin_test[1]} 📑
Test javoblari : {fin_test[2].upper()} ({len(fin_test[2])} ta savol) ❓ 
Test narxi : Bepul 🪙
                    """, parse_mode='html', reply_markup=mrk.mainMenu, document=fin_test[4])
        await state.finish()


    elif dt['ok'] == 'no':
        await state.finish()
        await call.answer("Bekor qilindi❌", show_alert=True)
        await call.message.edit_text("Bo'limlardan birini tanlang:", reply_markup=mrk.testMenu)


    elif dt['ok'] == 'other_test':
        try:
            test = db.get_random_free_test_by_unit(unit=dt['unit'], not_test_id=dt['test_id'])
            await state.update_data(test_id=test[0])

            await call.message.edit_text(f"""
Test ID : {test[0]} 🆔
Test mavzusi : {test[1]} 📑
Test javoblari : {test[2].upper()} ({len(test[2])} ta savol) ❓ 
Test narxi : Bepul 🪙

Ushbu testni olasizmi (Bepul)?
                """, reply_markup=mrk.okMenu)
            await st.get_free_test.ok.set()

        except:
            await call.answer("Ushbu mavzu bo'yicha faqat 1 ta test mavjud (", show_alert=True)
            await st.get_free_test.ok.set()




#   Buyurtma berish
@dp.callback_query_handler(text='ordering')
async def ncdcsdbcsjo(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer("""
Testlarga buyurtma berish uchun <a href="t.me/matematika_2_maktab" ><strong>admin</strong></a> bilan bog'lanishingizga to'g'ri keladi📲
""",parse_mode='html')
    await call.message.answer("Bo'limlardan birini tanlang", reply_markup=mrk.testMenu)




