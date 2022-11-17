
from aiogram.types import CallbackQuery
from aiogram import types

from app import bot, dp, db, st, cfg
from keyboards import admin_mrk as adm

from aiogram.dispatcher import FSMContext


#Cancel State 
@dp.message_handler(state=st.delMavzu, text='/cancel')
async def cancel_setNewMavzu(message, state:FSMContext):
    await state.finish()
    await message.answer("So'rov bekor qilindi ❌", reply_markup=adm.mainMenu)


# State 

@dp.callback_query_handler(user_id=cfg.ADMINS, text="Mavzuni o'chirish➖")
async def del_Mavzu(call:CallbackQuery, state:FSMContext):
    await call.message.delete()
    mavzular =  db.get_mavzular()
    mavzular2 = []

    for i,val in enumerate(mavzular, start=1):
        if int(val[2]) == 0:
            test = f'{i}) ID: `{val[0]}` | *{val[1]}* 🆓'
        else:
            test = f'{i}) ID: `{val[0]}` | *{val[1]}*'
        mavzular2.append(test)

    await call.message.answer('\n'.join(mavzular2), parse_mode='Markdown')
    await call.message.answer("Mavzu oldidagi ID raqamni ustiga bosib ko'chirib olib botga yuboring:")
    await st.delMavzu.id.set()




@dp.message_handler(user_id=cfg.ADMINS, state=st.delMavzu.id)
async def del_mavzu_pr(message, state:FSMContext):
    if message.text.isdigit():
        await state.update_data(id=message.text)
        data = await state.get_data()
        idMavzu = data['id']
        result = db.get_mavzu(idMavzu=idMavzu)
        
        if int(result[2]) == 0:
            narx = 'Bepul'

        else:
            narx = result[2] + "so'm"


        if result:
            await bot.send_document(chat_id=message.chat.id,document=result[4],caption=f"""
ID : {result[0]} 🆔
Mavzu : {result[1]} 📜
Narx : {narx:,} 💵

Mavzuda:
    ○
{result[3]}
    ○
            """)

            await message.answer("Rostdan ham ushbu mavzuni o'chirmoqchimisiz?", reply_markup=adm.okMenu)
            await st.delMavzu.next()
        else:
            await message.answer("Bunday ID dagi mavzu mavjud emas !", reply_markup=adm.mainMenu)
            await state.finish()

    else:
        await message.answer("Iltimos ID ni faqat raqamlarda yuboring ❗")
        await st.delMavzu.id.set()



@dp.callback_query_handler(user_id=cfg.ADMINS, state=st.delMavzu.ok)
async def ok_delMavzu(call:CallbackQuery, state:FSMContext):
    await state.update_data(ok=call.data)
    data = await state.get_data()

    if data['ok'] == 'yes':
        result = db.remove_Mavzu(data['id'])
        await call.answer("Mavzu muvaffaqiyatli o'chirildi✅", show_alert=True)
        await call.message.answer("Bosh menyu🏠", reply_markup=adm.mainMenu)

    if data['ok'] == 'no':
        await call.answer("Mavzu o'chirilmadi❌", show_alert=True)
        await call.message.answer("Bosh menyu🏠", reply_markup=adm.mainMenu)

    
    await state.finish()










