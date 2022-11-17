from aiogram.types import CallbackQuery
from aiogram import types
from app import bot, dp, db, st, cfg
from keyboards import admin_mrk as adm
from aiogram.dispatcher import FSMContext


@dp.message_handler(text="Buyurtmalar bo'limi📦")
async def asdwoenj(m:types.Message):
    await m.answer(m.text, reply_markup=adm.ReplyKeyboardRemove())
    await m.answer("Tanlang:", reply_markup=adm.orderMenu)


#Cancel State 
@dp.message_handler(state=st.act_reedem, text='/cancel')
async def cancel_act_reedem(message, state:FSMContext):
    await state.finish()
    await message.answer("So'rov bekor qilindi ❌", reply_markup=adm.mainMenu)


@dp.callback_query_handler(text='activate_reedem', user_id=cfg.ADMINS)
async def act_reedem(call:CallbackQuery, state:FSMContext):
    await call.message.delete()
    await call.message.answer("Aktivlash uchun buyurtma kodini kiriting:")
    await st.act_reedem.code_act.set()


@dp.message_handler(user_id=cfg.ADMINS, state=st.act_reedem.code_act)
async def ok_actReedem(message:types.Message, state:FSMContext):
    await state.update_data(code_act=message.text)
    data = await state.get_data()
    reedem = data['code_act']

    result = db.get_reedem(code=reedem)
    if result:
            if result[1] == 'mavzu':
                mv = db.get_mavzu(idMavzu=result[2])
                for m in mv:
                        await message.answer_document(
                            document=m[4],
                            caption=f"""
Mavzu ID : {m[0]} 🆔
Mavzu nomi: {m[1]} 📑
Mavzu narxi: {m[2]} so'm 🪙

Mavzu haqida:
➖
{m[3]}
➖
                            """
                        )
                        await message.answer("Mazvu kodi aktivlashtirilsinmi ?", reply_markup=adm.okMenu)

                await st.act_reedem.ok_act.set()

            if result[1] == 'test':
                mv = db.get_test(idTest=result[2])
                for m in mv:
                        await message.answer_document(
                            document=m[4],
                            caption=f"""
Test ID : {m[0]} 🆔
Test mavzusi: {m[1]} 📑
Test narxi: {m[3]} so'm 🪙
Test javoblari: {m[2].upper()} ({len(m[2])} ta savol)
                            """
                        )
                        await message.answer("Mazvu kodi aktivlashtirilsinmi ?", reply_markup=adm.okMenu)

                await st.act_reedem.ok_act.set()
                


    else:
        await message.answer("Bazada bunday aktivlash kodi mavjud emas (qayta kiritib ko'ring) ❌\n/cancel - Bekor qilish uchun", reply_markup=adm.mainMenu)
    
    await st.act_reedem.ok_act.set()
    




@dp.callback_query_handler(user_id=cfg.ADMINS, state=st.act_reedem.ok_act)
async def set_act_reedem(call:CallbackQuery, state:FSMContext):
    await state.update_data(ok_act = call.data)
    dt = await state.get_data()
    ans = dt['ok_act']
    reed = dt['code_act']
    if ans == 'yes':
        
        r = db.activate_reedem(reedem_code=reed)
        if r == True:
            await call.message.answer("Kod muvaffaqiyatli aktivlashtirildi✅", reply_markup=adm.mainMenu)
            await state.finish()

        else:
            await call.message.answer("Kod qandaydir xato sababli aktivlashtirilmadi❌", reply_markup=adm.mainMenu)
            await state.finish()

    else:
        await state.finish()
        await call.message.delete()
        await call.message.answer("So'rov bekor qilindi ❌", reply_markup=adm.mainMenu)






