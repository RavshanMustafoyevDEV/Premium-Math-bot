
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
    InlineKeyboardButton("Mavzu kodini aktivlash✅", callback_data="activate_reedem")
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










