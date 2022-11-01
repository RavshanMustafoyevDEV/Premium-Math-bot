from aiogram.types import CallbackQuery
from app import bot, dp, db, st
from app import mrk
from aiogram import types
from aiogram.dispatcher import FSMContext




@dp.message_handler(state=st.searchMavzu, text='/cancel')
async def cancel_setNewMavzu(message, state:FSMContext):
    await state.finish()
    await message.answer("So'rov bekor qilindi ❌", reply_markup=mrk.mainMenu)




@dp.callback_query_handler(text="search_mavzu")
async def start_searchMavzu(call:CallbackQuery):
    await call.message.delete()

    await call.message.answer("Qidirayotgan mavzungiz ID sini kiriting🆔✅:", reply_markup=mrk.ReplyKeyboardRemove())

    await st.searchMavzu.id.set()


@dp.message_handler(state=st.searchMavzu.id)
async def search_mavzu(message, state:FSMContext):

    if message.text.isdigit():
        await state.update_data(id=message.text)
        data = await state.get_data()
        idMavzu = data['id']
        result = db.get_mavzu(idMavzu=idMavzu)

        if result:
            for mavzu in result:
                if int(mavzu[2]) == 0:
                    await bot.send_document(
                        chat_id=message.chat.id, 
                        document=mavzu[4],
                        reply_markup=mrk.mainMenu,
                        parse_mode='Markdown',
                        caption=f"""
-----------------------------
ID: `{mavzu[0]}` 🆔
Mavzu: *{mavzu[1]}* 📑
Narxi: Bepul 💵

Mavzuda:
    ○
{mavzu[3]}
    ○
-----------------------------
                        """
                    )

                else:
                    await message.answer(f"""
-----------------------------
ID: `{mavzu[0]}` 🆔
Mavzu: *{mavzu[1]}* 📑
Narxi: {int(mavzu[2]):,} so'm 💵

Mavzuda:
    ○
{mavzu[3]}
    ○
-----------------------------                    
                    """, parse_mode='markdown', reply_markup=mrk.mainMenu)


        else:
            await message.answer("Bunday ID dagi mavzu mavjud emas ❗", reply_markup=mrk.mainMenu)


    else:
        await message.answer("Iltimos ID ni faqat raqamlarda kiriting ❗:")
        await st.searchMavzu.id.set()

    await state.finish()





