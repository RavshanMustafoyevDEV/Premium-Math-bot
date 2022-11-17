from aiogram.types import CallbackQuery
from aiogram import types
from app import bot, dp, db, st, cfg
from keyboards import admin_mrk as adm
from aiogram.dispatcher import FSMContext



@dp.message_handler(state=st.remove_test,text='/cancel')
async def jsdbfjs(message, state:FSMContext):
    await state.finish()
    await message.answer("Bekor qilindi❌", reply_markup=adm.mainMenu)


@dp.callback_query_handler(text='remove_test')
async def sdbdvfer(call:CallbackQuery):
    await call.message.edit_text("O'chirmoqchi bo'lgan test ID sini kiriting:\nBekor qilish uchun❌ - /cancel")
    await st.remove_test.test_id.set()


@dp.message_handler(state=st.remove_test.test_id)
async def dsjfneirn(message:types.Message, state:FSMContext):
    await state.update_data(test_id = message.text)
    dt = await state.get_data()
    r = db.get_test(idTest=dt['test_id'])
    if r: # Agar r mavjud bo'lsa:
        for i in r:
            if i[3] == '0':
                price = "Bepul"
            else:
                price = str(i[3]) + " so'm"
            await message.answer_document(
                document=i[4], 
                caption=f"""
ID : {i[0]} 🆔
Test mavzusi : {i[1]} 📑
Test narxi : {price} 🪙
Test javoblari : {i[2]}

Test o'chirilsinmi❓🗑️
                """,
                reply_markup=adm.okMenu
            )

    else:
        await state.finish()
        await message.answer("Bunday ID dagi test bazada mavjud emas !", reply_markup=adm.mainMenu)

    await st.remove_test.next()


@dp.callback_query_handler(state=st.remove_test.ok)
async def snjcjsbc(call:CallbackQuery, state:FSMContext):
    await state.update_data(ok = call.data)
    dt = await state.get_data()

    if dt['ok'] == 'yes':
        db.remove_test(idTest=dt['test_id'])
        await call.message.delete()
        await state.finish()
        await call.answer("Test o'chirildi✅🗑️", show_alert=True)
        await call.message.answer("Bo'limlardan birini tanlang:", reply_markup=adm.testMenu)


    elif dt["ok"] == 'no':
        await call.message.delete()
        await state.finish()
        await call.message.answer("Bo'limlardan birini tanlang:", reply_markup=adm.testMenu)
        await call.answer("Xatolik : Test o'chirilmadi❌", show_alert=True)


