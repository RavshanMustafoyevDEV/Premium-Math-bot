from aiogram.dispatcher.filters.state import State, StatesGroup

#Admin panelda yangi mavzu qo'shish
class newMavzu(StatesGroup):
    name = State()
    price = State()
    about = State()
    file_id = State()
    ok = State()

#Admin Panelda mavzuni o'chirish
class delMavzu(StatesGroup):
    id = State()
    ok = State()

# Mavzuni qidirish
class searchMavzu(StatesGroup):
    id = State()


#Mavzuni sotib olish
class buyMavzu(StatesGroup):
    id = State()



# Buyurtma kodini aktivlash 
class act_reedem(StatesGroup):
    code = State()
    ok = State()




# Sotib olingan 
class get_order_mavzu(StatesGroup):
    code = State()



