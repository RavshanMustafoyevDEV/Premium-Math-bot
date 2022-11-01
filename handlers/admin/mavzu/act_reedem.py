from aiogram.types import CallbackQuery
from app import bot, dp, db, st, cfg, types
from keyboards import admin_mrk as adm

from aiogram.dispatcher import FSMContext


#Cancel State 
@dp.message_handler(state=st.act_reedem, text='/cancel')
async def cancel_act_reedem(message, state:FSMContext):
    await state.finish()
    await message.answer("So'rov bekor qilindi ❌", reply_markup=adm.mainMenu)


@dp.callback_query_handler(text='activate_reedem', user_id=cfg.ADMINS)
async def act_reedem(call:CallbackQuery, state:FSMContext):
    await call.message.delete()
    await call.message.answer("Aktivlash uchun buyurtma kodini kiriting:")
    await st.act_reedem.code.set()


@dp.message_handler(user_id=cfg.ADMINS, state=st.act_reedem.code)
async def ok_actReedem(message:types.Message, state:FSMContext):
    await state.update_data(code=message.text)
    data = await state.get_data()
    reedem = data['code']

    result = db.get_mavzu_reedem(reedem)
    if result:
        await message.answer(result)
        await st.act_reedem.ok.set()

    else:
        await message.answer("Bazada bunday aktivlash kodi mavjud emas ❌", reply_markup=adm.mainMenu)
        await state.finish()
    
    await state.finish()




@dp.callback_query_handler(user_id=cfg.ADMINS, state=st.act_reedem.ok)
async def set_act_reedem(call:CallbackQuery, state:FSMContext):
    await state.update_data(code=call.data)
    data = await state.get_data()
    result = data['ok']


    



