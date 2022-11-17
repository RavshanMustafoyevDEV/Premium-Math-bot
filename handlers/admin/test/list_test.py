from aiogram.types import CallbackQuery
from aiogram import types
from app import bot, dp, db, st, cfg
from keyboards import admin_mrk as adm
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(text='back_test_admin')
async def hbjebr(call:CallbackQuery):
    await call.message.edit_text("Bo'limlardan birini tanlang:", reply_markup=adm.testMenu)


@dp.callback_query_handler(text='back_test_admin',state=st.list_test.test_unit, user_id=cfg.ADMINS)
async def hbjebr(call:CallbackQuery, state:FSMContext):
    await state.finish()
    await call.message.edit_text("Bo'limlardan birini tanlang:", reply_markup=adm.testMenu)



@dp.callback_query_handler(text='list_tests', user_id=cfg.ADMINS)
async def list_test(call:CallbackQuery):
    units_menu = adm.InlineKeyboardMarkup(row_width=2)
    units_menu.add(adm.InlineKeyboardButton("Barcha testlar📑", callback_data='all_tests'))
    for i in db.list_unit():
        units_menu.insert(
            adm.InlineKeyboardButton(text=i[0], callback_data=i[0]),
        )

    units_menu.row(adm.InlineKeyboardButton("Orqaga🔙", callback_data='back_test_admin'))


    await call.message.edit_text("Test mavzusini tanlang:", reply_markup=units_menu)
    await st.list_test.test_unit.set()



@dp.callback_query_handler(state=st.list_test.test_unit, user_id=cfg.ADMINS)
async def jhsdbcjsdhb(call:CallbackQuery, state:FSMContext):
    back_testlar = adm.InlineKeyboardMarkup().add(
        adm.InlineKeyboardButton("Orqaga🔙", callback_data='back_test_admin')
    )

    await state.update_data(test_unit=call.data)
    dt = await state.get_data()

    if dt['test_unit'] == 'all_tests':
        testlar = db.get_all_tests()
    else:
        testlar = db.get_test_by(unit=dt['test_unit'])

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
        """, parse_mode='html', reply_markup=back_testlar)

    else:
        await state.finish()
        await call.message.edit_text("Bu mavzudagi testlar yaqin vaqtlar ichida qo'shiladi )", reply_markup=back_testlar)




