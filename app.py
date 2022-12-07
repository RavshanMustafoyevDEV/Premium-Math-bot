from aiogram import Bot, Dispatcher, executor, types
#FSM import
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage



import states.state as st
import keyboards.markups as mrk
import keyboards
import config as cfg
from data import database




bot = Bot(cfg.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
adminID = cfg.ADMINS
db = database.Database('data/data.db')










if __name__ == '__main__':
    #hanlers import
    from handlers.user.user import dp
    from handlers.user.mavzu.mavzular import dp
    from handlers.admin.admin import dp
    from handlers.admin.mavzu.set_newMavzu import dp
    from handlers.admin.mavzu.del_Mavzu import dp
    from handlers.admin.mavzu.list_mavzu import dp
    from handlers.user.mavzu.search_Mavzu import dp
    from handlers.user.mavzu.buy_mavzu import dp
    from handlers.user.delReedem import dp
    from handlers.user.test.tests import dp
    from handlers.admin.test.newTest import dp
    from handlers.admin.orders.order import dp
    from handlers.admin.units.unit import dp
    from handlers.admin.test.search_test import dp
    from handlers.admin.test.list_test import dp
    from handlers.admin.test.remove_test import dp
    from handlers.user.test.buy_test import dp
    from handlers.user.test.check_test import dp
    from handlers.user.test.list_test import dp
    from handlers.user.test.my_tests import dp
    from handlers.admin.bot.bot_settings import dp




  
    executor.start_polling(dp, skip_updates=False)