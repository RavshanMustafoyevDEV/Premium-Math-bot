from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardRemove


# Your Code

#User Markup
#Main Menu
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).row(
    KeyboardButton('Mavzular📃'),
    KeyboardButton('Testlar📑'),
    KeyboardButton('Buyurtma📦'),
)


#Registration menu
regMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Ro'yxatdan o'tish", request_contact=True)
)

list_mavzu_menu2 = InlineKeyboardMarkup().add(
    InlineKeyboardButton("Mavzuni qidirish🔍", callback_data='search_mavzu')
)

# Mavzular Main menu
mavzularMenu = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("Mavzu kursini xarid qilish🛒", callback_data="buy_mavzu")
    ).row(
    InlineKeyboardButton("Ro'yxat📜", callback_data='list_mavzular'),
    InlineKeyboardButton("Mavzuni qidirish🔍", callback_data='search_mavzu')
    ).add(
    InlineKeyboardButton('Mening mavzularim📔', callback_data='my_mavzular'),
    InlineKeyboardButton("Bosh menyu🏠", callback_data='mainMenuUser'),
)

myMavzuMenu = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("Orqaga🔙", callback_data='back_mavzu_user')
)


buy_mavzuMenu = InlineKeyboardMarkup().add(
    InlineKeyboardButton("Ro'yxat📜", callback_data='list_mavzular')
)


# buyurtm menu
buyurtmaMenu = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("Buyurtmani olish📩", callback_data='get_orderMavzu'),
    InlineKeyboardButton("Bosh menyu🏠", callback_data='mainMenuUser')

)



mavzu_typeMenu = InlineKeyboardMarkup().add(
    InlineKeyboardButton("Premium mavzular🪙", callback_data='get_premium_mavzular'),
    InlineKeyboardButton("Bepul mavzular✅", callback_data="get_free_mavzular"),
)






#    TESTLAR---------------------------------------------------
testMenu = InlineKeyboardMarkup(row_width=1).row(
    InlineKeyboardButton("Ro'yxat📑", callback_data='list_tests_user'),
    InlineKeyboardButton('Test xarid qilish🛒', callback_data='buy_test'),
).add(
    InlineKeyboardButton('Test javobini tekshirish✅', callback_data='check_test'),
    InlineKeyboardButton("Mening testlarim📜", callback_data='my_tests_user'),
    InlineKeyboardButton("Orqaga🔙", callback_data='mainMenuUser')
)


type_testMenu = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("Bepul tayyor testlar🆓", callback_data='free_tests'),
    InlineKeyboardButton("Pullik tayyor testlar🪙", callback_data='pre_tests'),
    InlineKeyboardButton("Testga buyurtma berish🛒", callback_data='ordering'),
    InlineKeyboardButton("Orqaga🔙", callback_data='back_test_user')
)


okMenu = InlineKeyboardMarkup(row_width=1).row(
    InlineKeyboardButton("Ha✅", callback_data='yes'),
    InlineKeyboardButton("Bekor qilish❌", callback_data='no'),
).add(
    InlineKeyboardButton("Boshqa test♻️", callback_data='other_test')
)



back_testlar_user = InlineKeyboardMarkup().add(
    InlineKeyboardButton("Orqaga🔙", callback_data='back_test_user')
)

my_testsMenu = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton('Test javobini tekshirish✅', callback_data='check_test'),
    InlineKeyboardButton("Orqaga🔙", callback_data='back_test_user')
)