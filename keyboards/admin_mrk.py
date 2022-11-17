
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardRemove
from handlers.user.user import db

# Your Code

#Admin Markup
#Main Menu
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(
    KeyboardButton("Mavzular bo'limi📃"),
    KeyboardButton("Testlar bo'limi📑"),
    KeyboardButton("Buyurtmalar bo'limi📦"),
)

mavzularMenu = InlineKeyboardMarkup().row(
    InlineKeyboardButton('Yangi mavzu➕', callback_data='Yangi mavzu➕'),
    InlineKeyboardButton("Mavzuni o'chirish➖", callback_data="Mavzuni o'chirish➖"),
).add(
    InlineKeyboardButton("Ro'yxat📑", callback_data="Ro'yxat📑") ,
).row(
    InlineKeyboardButton("Bosh menyu🏠", callback_data="mainMenu")  
)


mavzuMenu = InlineKeyboardMarkup()

for mavzu in db.get_mavzular():
    mavzuMenu.add(
        InlineKeyboardButton(text=f'{mavzu[1]}', callback_data=f'{mavzu[1]}'),
    )


act_reedemMenu = InlineKeyboardMarkup().add(
    InlineKeyboardButton("Ha", callback_data='act'),
    InlineKeyboardButton("Yo'q", callback_data='de-act')
)




okMenu = InlineKeyboardMarkup().add(
    InlineKeyboardButton("Ha", callback_data='yes'),
    InlineKeyboardButton("Yo'q", callback_data='no')
)

newTest_okMenu = InlineKeyboardMarkup().add(
    InlineKeyboardButton("Ha", callback_data='ha'),
    InlineKeyboardButton("Yo'q", callback_data='yo')
)




# TESTS----------------------------------------------------------------
testMenu = InlineKeyboardMarkup(row_width=1).row(
    InlineKeyboardButton("Qo'shish➕", callback_data='add_test'),
    InlineKeyboardButton("O'chirish➖", callback_data='remove_test'),
).row(
    InlineKeyboardButton("Ro'yxat📑", callback_data='list_tests'),
    InlineKeyboardButton("Qidirish🔍", callback_data='search_test')
).add(
    InlineKeyboardButton("Unitlar", callback_data="units"),
    InlineKeyboardButton("Orqaga🔙", callback_data='mainMenu')
)










# ORDERS ------------------------------------------------
orderMenu = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("Kod aktivlashtirish✅", callback_data='activate_reedem'),
    InlineKeyboardButton("Orqaga🔙", callback_data='mainMenu')
)











# UNITS==================================================================


unitMainMenu = InlineKeyboardMarkup(row_width=1).row(
    InlineKeyboardButton("Qo'shish➕", callback_data="add_unit"),
    InlineKeyboardButton("O'chirish➖", callback_data="remove_unit"),
).add(
    InlineKeyboardButton("Ro'yxat📜", callback_data="list_unit"),
    InlineKeyboardButton("Orqaga🔙", callback_data="back_tests"),
)




