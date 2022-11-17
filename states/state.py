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
    code_act = State()
    ok_act = State()




# Sotib olingan 
class get_order(StatesGroup):
    code = State()



# TESTS--------------------------------------------------------------------------
class new_test(StatesGroup):
    unit = State()
    answers = State()
    price = State()
    file_id = State()
    ok = State()

class remove_test(StatesGroup):
    test_id = State()
    ok = State()


class search_test(StatesGroup):
    test_id = State()

class list_test(StatesGroup):
    test_unit = State()



class list_test2(StatesGroup):
    unit = State()



class buyTest(StatesGroup):
    unit = State()
    test_id = State()
    ok = State()



class get_free_test(StatesGroup):
    unit = State()
    test_id = State()
    ok = State()


class check_test_answers(StatesGroup):
    test_id = State()
    test_answers = State()








#UNITS=======================================================
class new_unit(StatesGroup):
    unit = State()

class remove_unit(StatesGroup):
    unit = State()


