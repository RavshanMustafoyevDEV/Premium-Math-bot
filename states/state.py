from aiogram.dispatcher.filters.state import State, StatesGroup

class newMavzu(StatesGroup):
    name = State()
    price = State()
    about = State()
    file_id = State()
    ok = State()


class delMavzu(StatesGroup):
    id = State()
    ok = State()


class searchMavzu(StatesGroup):
    id = State()


class buyMavzu(StatesGroup):
    id = State()

class act_reedem(StatesGroup):
    code = State()


class get_order_mavzu(StatesGroup):
    code = State()




