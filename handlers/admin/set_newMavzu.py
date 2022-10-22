from aiogram.types import CallbackQuery
from aiogram import types

from app import bot, dp, db, st, cfg
from keyboards import admin_mrk as adm

from aiogram.dispatcher import FSMContext

@dp.message_handler(user_id=cfg.ADMINS, text="Mavzular bo'limi📃")
async def MavzularMenu(message):
    await message.answer(text=message.text, reply_markup=adm.ReplyKeyboardRemove())
    await message.answer(
        text="Bo'limlardan birini tanlang:",
        reply_markup=adm.mavzularMenu
    )


@dp.message_handler(state=st.newMavzu, text='/cancel')
async def cancel_setNewMavzu(message, state:FSMContext):
    await state.finish()
    await message.answer("So'rov bekor qilindi ❌", reply_markup=adm.mainMenu)


@dp.callback_query_handler(user_id=cfg.ADMINS, text='Yangi mavzu➕')
async def call_new_mavzu(call:CallbackQuery):
    await call.message.edit_text("Yangi mavzu nomini kiriting:")
    await st.newMavzu.name.set()


@dp.message_handler(user_id=cfg.ADMINS, state=st.newMavzu.name)
async def set_newMavzu_name(message, state:FSMContext):
    await state.update_data(name=message.text)
    await message.answer(
    """
    Yangi mavzu narxini yuboring:

    (Narxni faqat raqamlardan hech qanday so'z yoki probellarsiz yozing!)
    (Masalan: 20000)
    """
    )
    await st.newMavzu.next()

@dp.message_handler(user_id=cfg.ADMINS, state=st.newMavzu.price)
async def set_newMavzu_price(message, state:FSMContext):
    m = message.text
    if m.isdigit():
        if message.text == '0':
            await state.update_data(price="0")
        else:
            await state.update_data(price=message.text)
        
        await message.answer("Yangi mavzu haqida yozing:")
        await st.newMavzu.next()

    else:
        await message.answer("Iltimos narxni hech qanday probellarsiz faqat raqamlarda kiriting ❗")
        await st.newMavzu.price.set()



@dp.message_handler(user_id=cfg.ADMINS, state=st.newMavzu.about)
async def set_newMavzu_about(message, state:FSMContext):
    await state.update_data(about=message.text)
    await message.answer("Yangi mavzu faylini jo'nating:")
    await st.newMavzu.next()


@dp.message_handler(user_id=cfg.ADMINS, state=st.newMavzu.file_id, content_types=['document'])
async def set_newMavzu_file(message, state:FSMContext):
    await state.update_data(file_id=message.document.file_id)
    data = await state.get_data()


    await bot.send_document(message.chat.id, data['file_id'], caption=f"""
Mavzu : {data['name']} 📜

Mavzu nimadan iborat📑 : 
○
{data['about']}
○

Narxi : {data['price']} so'm 💵   
    """)

    await message.answer(f"""
Yangi mavzuni to'g'ri kiritdingizmi ?
    """, reply_markup=adm.okMenu)


    await st.newMavzu.next()

@dp.callback_query_handler(user_id=cfg.ADMINS, state=st.newMavzu.ok)
async def set_ok(call:CallbackQuery, state:FSMContext):
    await state.update_data(ok=call.data)
    data = await state.get_data()

    if data['ok'] == 'yes': # Agar ok ha bo'lsa
        await state.finish()
        result = db.set_newMavzu(name=data['name'], price=data['price'], about=data['about'], file_id=data['file_id'])

        if result == True:
            await call.answer('Yangi mavzu kiritildi✅', show_alert=True)
            await call.message.delete()
            await call.message.answer("Bosh menyu🏠", reply_markup=adm.mainMenu)

        else:
            await call.answer("Ushbu mavzu avval bazaga qo'shilgan uni o'xgartirihs uchun eski mavzuni o'chirib yangisini qayta kiriting ❗", show_alert=True)
            await call.message.delete()
            await call.message.answer("Bosh menyu🏠", reply_markup=adm.mainMenu)
        

    elif data['ok'] == 'no':
        await state.reset_data()
        await call.answer('Yangi mavzu bekor qilindi❌', show_alert=True)
        await call.message.delete()
        await call.message.answer("Bosh menyu🏠", reply_markup=adm.mainMenu)

    else:
        pass




























