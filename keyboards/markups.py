from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardRemove


# Your Code

#User Markup
#Main Menu
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).row(
    KeyboardButton('Mavzular📃'),
    KeyboardButton('Testlar📑'),
    KeyboardButton('Buyurtma📦'),
).add(
    KeyboardButton('Izoh qoldirish📜')
)


#Registration menu
regMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Ro'yxatdan o'tish", request_contact=True)
)



# Mavzular Main menu
mavzularMenu = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("Mavzu kursini xarid qilish🛒", callback_data="buy_mavzu")
    ).row(
    InlineKeyboardButton("Ro'yxat📜", callback_data='list_mavzular'),
    InlineKeyboardButton("Mavzuni qidirish🔍", callback_data='search_mavzu')
    ).add(
    InlineKeyboardButton("Bosh menyu🏠", callback_data='mainMenuUser')
)


buy_mavzuMenu = InlineKeyboardMarkup().add(
    InlineKeyboardButton("Ro'yxat📜", callback_data='list_mavzular')
)


# buyurtm menu
buyurtmaMenu = InlineKeyboardMarkup().add(
    InlineKeyboardButton("Buyurtmani olish📩", callback_data='get_orderMavzu'),
    InlineKeyboardButton("Bosh menyu🏠", callback_data='mainMenuUser')

)



mavzu_typeMenu = InlineKeyboardMarkup().add(
    InlineKeyboardButton("Premium mavzular🪙", callback_data='get_premium_mavzular'),
    InlineKeyboardButton("Bepul mavzular✅", callback_data="get_free_mavzular"),
)


