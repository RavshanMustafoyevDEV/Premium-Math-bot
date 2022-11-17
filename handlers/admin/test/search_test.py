from aiogram.types import CallbackQuery
from aiogram import types
from app import bot, dp, db, st, cfg
from keyboards import admin_mrk as adm
from aiogram.dispatcher import FSMContext



@dp.callback_query_handler(text='search_test', user_id=cfg.ADMINS)
async def kdsnncjs(call:CallbackQuery, state:FSMContext):
    await call.message.edit_text("Qidirmoqchi bo'lgan test ID sini kiriting:")
    await st.search_test.test_id.set()

@dp.message_handler(state=st.search_test.test_id, user_id=cfg.ADMINS)
async def hsdbcjsh(message:types.Message, state:FSMContext):
    await state.update_data(test_id=message.text)
    dt = await state.get_data()
    r = db.get_test(idTest=dt['test_id'])
    if r:
        for i in r:
            if i[3] == 0:
                price = 'Bepul'
            else:
                price = str(i[3]) + " so'm"

            

            await message.answer_document(caption=f"""
Test ID: <code>{i[0]}</code> 🆔
Test mavzusi: <strong>{i[1]}</strong> 📜
Test narxi: {price} 🪙
Test javoblari : {i[2].upper()} ({len(i[2])} ta savol)📑
            """,document=i[4], reply_markup=adm.mainMenu, parse_mode='html'
            )
        await state.finish()

    else:
        await message.answer("Bunday ID dagi test mavjud emas❌", reply_markup=adm.mainMenu)
        await state.finish()






