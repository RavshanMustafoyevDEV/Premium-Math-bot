from aiogram.types import CallbackQuery
from aiogram import types
from app import bot, dp, db, st, cfg
from keyboards import admin_mrk as adm
from aiogram.dispatcher import FSMContext





@dp.callback_query_handler(text='units')
async def jbdjwhe(call:CallbackQuery):
    await call.message.edit_text("Bo'limlardan birini tanlang:", reply_markup=adm.unitMainMenu)







# YANGI UNIT
@dp.message_handler(text='/cancel', state=st.new_unit)
async def cancel(message, state:FSMContext):
    await state.finish()
    await message.answer("Bekor qilindi❌", reply_markup=adm.mainMenu)

@dp.callback_query_handler(text='add_unit')
async def ihvbdeubjrhgf(call:CallbackQuery, state:FSMContext):
    await call.message.delete()
    await call.message.answer("Yangi unit nomini kiriting:", reply_markup=adm.ReplyKeyboardRemove())
    await st.new_unit.unit.set()

@dp.message_handler(state=st.new_unit.unit)
async def hsdbcuwsh(message:types.Message, state:FSMContext):
    await state.update_data(unit = message.text)
    dt = await state.get_data()
    db.new_unit(unit=dt['unit'])
    await message.answer("Yangi unit bazaga qo'shildi✅", reply_markup=adm.mainMenu)
    await state.finish()



# UNITNI o'chirish
@dp.message_handler(text='/cancel', state=st.remove_unit)
async def cancerergl(message, state:FSMContext):
    await state.finish()
    await message.answer("Bekor qilindi❌", reply_markup=adm.mainMenu)

@dp.callback_query_handler(text='remove_unit')
async def ihvbder45ubjrhgf(call:CallbackQuery, state:FSMContext):
    units_menu = adm.InlineKeyboardMarkup(row_width=2)
    for i in db.list_unit():
        units_menu.insert(
            adm.InlineKeyboardButton(text=i[0], callback_data=i[0]),
        )

    await call.message.delete()
    await call.message.answer("Qaysi unitni o'chirmoqchisiz?", reply_markup=units_menu)
    await st.remove_unit.unit.set()

@dp.callback_query_handler(state=st.remove_unit.unit)
async def hsdbregcuwsh(call:CallbackQuery, state:FSMContext):
    await state.update_data(unit = call.data)
    dt = await state.get_data()
    db.remove_unit(unit=dt['unit'])
    await call.message.delete()
    await call.message.answer("Unit o'chirildi✅🗑️", reply_markup=adm.mainMenu)
    await state.finish()



#LIST UNITS
@dp.callback_query_handler(text='list_unit')
async def hjsvbjfeh(call:CallbackQuery):
    back_units = adm.InlineKeyboardMarkup().add(
       adm.InlineKeyboardButton("Orqaga🔙", callback_data='back_unit') 
    )
    list = []
    r = db.list_unit()
    for i in r:
        list.append(i[0])

    fin_list = '\n'.join(list)
    await call.message.edit_text(f"""
Unitlar ro'yxati:📑

{fin_list}
    """, reply_markup=back_units)



@dp.callback_query_handler(text='back_unit')
async def hjsvbsddgjfeh(call:CallbackQuery):
    await call.message.edit_text("Tanlang:", reply_markup=adm.unitMainMenu)




