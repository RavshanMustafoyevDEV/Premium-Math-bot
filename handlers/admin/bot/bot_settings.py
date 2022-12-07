from aiogram.types import CallbackQuery
from aiogram import types
from app import bot, dp, db, st, cfg
from keyboards import admin_mrk as adm
from aiogram.dispatcher import FSMContext





@dp.callback_query_handler(text='back_to_bot')
async def back_to_bot(call:CallbackQuery):
    await call.message.edit_text("Bo'limlardan birini tanlang:", reply_markup=adm.botMenu)


@dp.message_handler(text="Bot🤖", user_id=cfg.ADMINS)
async def start_bot_settings(message:types.Message):
    await message.answer(message.text, reply_markup=adm.ReplyKeyboardRemove())
    await message.answer("Bo'limlardan birini tanlang:", reply_markup=adm.botMenu)


@dp.callback_query_handler(text='statistic', user_id = cfg.ADMINS)
async def users_total(call:CallbackQuery):
    tests = len(db.get_all_tests())
    mavzular = len(db.get_mavzular())
    users = len(db.get_users())
    saled_tests = db.get_saled_tests()

    await call.message.edit_text(f"""
Foydalanuvchilar soni : {users} ta👤
Testlar soni : {tests} ta 📑
Mavzular soni : {mavzular} ta 📜

Sotilgan testlar soni : {len(saled_tests)} ta ( {sum(saled_tests):,} so'm🪙 )
    """, reply_markup=adm.back_to_botMenu)











#New POst================================================

@dp.message_handler(text='/cancel', state=st.newPost)
async def cancel_post(message:types.Message, state:FSMContext):
    await state.finish()
    await message.answer("Bekor qilindi❌")
    await message.answer("Bo'limlardan birini tanlang:", reply_markup=adm.botMenu)



@dp.callback_query_handler(text='new_post')
async def start_new_post(call:CallbackQuery):
    await call.message.edit_text("Yangi postingizda rasm ishtirok etadimi ?", reply_markup=adm.okMenu)
    await st.newPost.isImg.set()

@dp.callback_query_handler(state=st.newPost.isImg)
async def isImg(call:CallbackQuery, state:FSMContext):
    await state.update_data(isImg = call.data)
    dt = await state.get_data()

    if dt['isImg'] == 'yes':
        await call.message.edit_text("Yangi post uchun rasmni yuboring : ")
        await st.newPost.img.set()

    else:
        await call.message.edit_text("Yangi postingiz tekstini yuboring")
        await st.newPost.message.set()


@dp.message_handler(content_types=types.message.ContentTypes.PHOTO, state=st.newPost.img)
async def set_image(message:types.Message, state:FSMContext):
    await state.update_data(img = message.photo[-1].file_id)
    await message.answer("Rasm qabul qilindi✅")
    await message.answer("Postingiz tekstini yuboring:")
    await st.newPost.message.set()



@dp.message_handler(state=st.newPost.message)
async def set_message(message:types.Message, state:FSMContext):
    await state.update_data(message=message.text)
    await message.answer("Tekstingiz qabul qilindi✅")
    dt = await state.get_data()


    if dt['isImg'] == 'yes':
        await message.answer_photo(
            photo=dt['img'],
            caption=f"""
{dt['message']}

Ushbu post foydalanuvchilarga yuborilsinmi ?
            """, reply_markup=adm.okMenu
        )

    else:
        await message.answer(
            text=f"""
{dt['message']}

Ushbu post foydalanuvchilarga yuborilsinmi ?
            """, reply_markup=adm.okMenu
        )

    await st.newPost.ok.set()


@dp.callback_query_handler(state=st.newPost.ok)
async def set_ok(call:CallbackQuery, state:FSMContext):
    await state.update_data(ok = call.data)
    dt = await state.get_data()

    if dt['ok'] == 'yes':
        await call.message.delete()
        await state.finish()
        users = db.get_users()

        if dt['isImg'] == 'yes':
            for user in users:
                try:
                    await bot.send_photo(
                        photo=dt['img'],
                        caption=dt['message'],
                        chat_id=user[0]
                    )
                except:
                    pass

        else:
            for user in users:
                try:
                    await bot.send_message(
                        text=dt['message'],
                        chat_id=user[0]
                    )
                except:
                    pass 

        await call.message.answer("Post muvaffaqiyatli jo'natildi✅")         

    else:
        await call.message.delete()
        await state.finish()
        await call.answer("Bekor qilindi❌", show_alert=True)
        await call.message.answer("Bo'limlardan birini tanlang:", reply_markup=adm.botMenu)










# ADMIN ADD REMOVE ============================================================================



