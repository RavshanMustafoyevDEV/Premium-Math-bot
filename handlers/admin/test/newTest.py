from aiogram.types import CallbackQuery
from aiogram import types
from app import bot, dp, db, st, cfg
from keyboards import admin_mrk as adm
from aiogram.dispatcher import FSMContext


@dp.message_handler(text='/cancel', state=st.new_test)
async def cancel(message, state:FSMContext):
    await state.finish()
    await message.answer("Bekor qilindi❌", reply_markup=adm.mainMenu)


@dp.message_handler(text="Testlar bo'limi📑", user_id=cfg.ADMINS)
async def tests_start(message:types.Message):
    await message.answer(message.text, reply_markup=adm.ReplyKeyboardRemove())
    await message.answer("Bo'limlardan birini tanlang:", reply_markup=adm.testMenu)


@dp.callback_query_handler(text='back_tests')
async def fgecdgw(call:CallbackQuery):
    await call.message.edit_text("Bo'limlardan birini tanlang:", reply_markup=adm.testMenu)



@dp.callback_query_handler(text='add_test')
async def add_testst(call:CallbackQuery, state:FSMContext):

    units_menu = adm.InlineKeyboardMarkup(row_width=2)
    for i in db.list_unit():
        units_menu.insert(
            adm.InlineKeyboardButton(text=i[0], callback_data=i[0]),
        )

    await call.message.delete()
    await call.message.answer("Yangi test kiritish boshlandi✅", reply_markup=adm.ReplyKeyboardRemove())
    await call.message.answer("Yangi test qaysi mavzuga asoslangan?", reply_markup=units_menu)
    await st.new_test.unit.set()

@dp.callback_query_handler(state=st.new_test.unit)
async def seta_unit(call:CallbackQuery, state:FSMContext):
    await state.update_data(unit = call.data)
    await call.message.edit_text("""
Yangi test javoblarini kiriting  :
DIQQAT savollar soni javoblar soni bilan mos kelishi kk e'tiborliroq bo'ling!

Masalan : abcdabcdba
    """)
    await st.new_test.next()



@dp.message_handler(state=st.new_test.answers)
async def bdhjfewh(m:types.Message, state:FSMContext):
    await state.update_data(answers=m.text)
    await m.answer("Yangi test narxini kiriting:")
    await st.new_test.next()



@dp.message_handler(state=st.new_test.price)
async def fuwbfe(m:types.Message, state:FSMContext):
    if m.text.isdigit():
        await state.update_data(price = m.text)
        await m.answer("Yangi test faylini jo'nating:")
        await st.new_test.next()
    else:
        await m.answer("Narx faqat raqamlardan iborat bo'lishi lozim!")
        await st.new_test.price.set()




@dp.message_handler(content_types=['document'], state=st.new_test.file_id)
async def idbscjhsb(m:types.Message, state:FSMContext):
    await state.update_data(file_id=m.document.file_id)
    dt = await state.get_data()
    await m.answer_document(document=dt['file_id'],caption=f"""
Test mavzusi: {dt['unit']} 📑
Test javoblari : {dt['answers'].upper()} ({len(dt['answers'])} ta savol)📜
Test narxi: {dt['price']} so'm🪙
    """)
    await m.answer("Testni to'g'ri kiritdingizmi?", reply_markup=adm.newTest_okMenu)
    await st.new_test.ok.set()





@dp.callback_query_handler(state=st.new_test.ok, user_id=cfg.ADMINS)
async def isvuknijfdgifdb(call:CallbackQuery, state:FSMContext):
    await state.update_data(ok = call.data)
    dt = await state.get_data()
    if dt['ok'] == 'ha':
        db.set_new_test(unit=dt['unit'], answers=dt['answers'], price=dt['price'], file_id=dt['file_id'])
        await call.message.edit_text("Test muvaffaqaiyatli bazaga qo'shildi✅")
        await state.finish()
        await call.message.answer("Admin Panel👤", reply_markup=adm.mainMenu)
    else:
        await state.reset_data()
        await call.message.edit_text("Bekor qilindi❌", reply_markup=adm.mainMenu)
