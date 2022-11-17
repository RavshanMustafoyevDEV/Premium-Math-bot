from aiogram.types import CallbackQuery
from app import bot, dp, db, st
from app import mrk
from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(text='/cancel', state=st.check_test_answers)
async def canc_check_test(message, state:FSMContext):
    await state.finish()
    await message.answer("Bekor qilindi❌", reply_markup=mrk.mainMenu)



@dp.callback_query_handler(text='check_test')
async def check_test(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer("Testingiz ID sini kiriting :\nBekor qilish uchun - /cancel ❌")
    await st.check_test_answers.test_id.set()

@dp.message_handler(state=st.check_test_answers.test_id)
async def set_check_test_id(message:types.Message, state:FSMContext):
    if message.text.isdigit()==True:
        if db.get_test(idTest=message.text):
            await state.update_data(test_id=message.text)
            await message.answer("""
Test javoblaringizni kiriting:

ESLATMA : Test javoblaringiz soni savollar soni bilan teng bo'lishi kerak ❗

<em>Masalan : abcdabcdab</em>
""", parse_mode='html')
            await st.check_test_answers.next()

        else:
            await state.finish()
            await message.answer("Bunday ID dagi test bazada mavjud emas qayta urinib ko'ring (", reply_markup=mrk.mainMenu)
    else:
        await state.finish()
        await message.answer("ID faqat raqamdan iborat bo'lishi kerak 🆔❌", reply_markup=mrk.mainMenu)


@dp.message_handler(state=st.check_test_answers.test_answers)
async def check_test_fin(message:types.Message, state:FSMContext):
    await state.update_data(test_answers=message.text)
    dt = await state.get_data()

    output = db.check_test_answers(test_id=dt['test_id'], test_answers=dt['test_answers'])
    await state.finish()
    await message.answer(output, reply_markup=mrk.mainMenu)

