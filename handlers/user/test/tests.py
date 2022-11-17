from aiogram.types import CallbackQuery
from app import bot, dp, db, st
from app import mrk
from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(text="Testlar📑")
async def start_tests(m:types.Message):
    await m.answer(m.text, reply_markup=mrk.ReplyKeyboardRemove())
    await m.answer("Tanlang:", reply_markup=mrk.testMenu)

@dp.callback_query_handler(text="buy_test")
async def kjbcw(call:CallbackQuery):
    await call.message.edit_text("Tanlang:", reply_markup=mrk.type_testMenu)

@dp.callback_query_handler(text='back_test_user', state=st.list_test2)
async def kjcndsferekj(call:CallbackQuery, state:FSMContext):
    await state.finish()
    await call.message.edit_text("Tanlang:", reply_markup=mrk.testMenu)

@dp.callback_query_handler(text='back_test_user')
async def kjcnekj(call:CallbackQuery):
    await call.message.edit_text("Tanlang:", reply_markup=mrk.testMenu)








