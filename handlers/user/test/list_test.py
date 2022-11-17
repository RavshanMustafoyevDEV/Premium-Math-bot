from aiogram.types import CallbackQuery
from app import bot, dp, db, st
from app import mrk
from aiogram import types
from aiogram.dispatcher import FSMContext






@dp.callback_query_handler(text='list_tests_user')
async def list_tefvdvfbrgbst(call:CallbackQuery):
    units_menu_user = mrk.InlineKeyboardMarkup(row_width=2)
    units_menu_user.add(mrk.InlineKeyboardButton("Barcha testlar📑", callback_data='all_tests'))
    for i in db.list_unit():
        units_menu_user.insert(
            mrk.InlineKeyboardButton(text=i[0], callback_data=i[0]),
        )
    
    await call.message.edit_text("Test mavzusini tanlang:", reply_markup=units_menu_user)
    await st.list_test2.unit.set()

@dp.callback_query_handler(state=st.list_test2.unit)
async def jdsbuerbub(call:CallbackQuery, state:FSMContext):
    
    await state.update_data(unit = call.data)
    dt = await state.get_data()

    if dt['unit'] == 'all_tests':
        testlar = db.get_all_tests()
    else:
        testlar = db.get_test_by(unit=dt['unit'])

    if testlar:
        testlar2 = []

        for i,val in enumerate(testlar, start=1):
            if int(val[3]) == 0:
                test = f'{i}) ID: <code>{val[0]}</code>  |  Test mavzusi: <strong>{val[1]}</strong> 🆓'
            else:
                test = f'{i}) ID: <code>{val[0]}</code>  |  Test mavzusi: <strong>{val[1]}</strong>'
            testlar2.append(test)

        fin_list = '\n'.join(testlar2)
        await state.finish()
        await call.message.edit_text(f"""
Testlar soni : {len(testlar)} ta 📚

Ro'yxat:
{fin_list}
        """, parse_mode='html', reply_markup=mrk.back_testlar_user)

    else:
        await state.finish()
        await call.message.edit_text("Bu mavzudagi testlar yaqin vaqtlar ichida qo'shiladi )", reply_markup=mrk.back_testlar_user)





