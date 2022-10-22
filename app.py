from cgitb import text
from aiogram import Bot, Dispatcher, executor, types
import asyncio
#FSM import
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage



import states.state as st
import keyboards.markups as mrk
import keyboards
import config as cfg
from data import database

loop = asyncio.new_event_loop()

bot = Bot(cfg.TOKEN)
dp = Dispatcher(bot, loop=loop, storage=MemoryStorage())
adminID = cfg.ADMINS
db = database.Database('data/data.db')










if __name__ == '__main__':
    #hanlers import
    from handlers.user.user import dp
    from handlers.user.mavzular import dp
    from handlers.admin.admin import dp
    from handlers.admin.set_newMavzu import dp
    from handlers.admin.del_Mavzu import dp
    from handlers.admin.list_mavzu import dp
    from handlers.user.search_Mavzu import dp
    from handlers.user.buy_mavzu import dp
    from handlers.admin.act_reedem import dp
    from handlers.user.delReedem import dp

  
    executor.start_polling(dp, skip_updates=False)