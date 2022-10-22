from aiogram_dialog import Window, Dialog, DialogRegistry, DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const

import states.state as st
import keyboards.markups as mrk
import keyboards
import config as cfg
from data import database
from app import dp

registry = DialogRegistry(dp)




registry.register(
    main_window = Window(
        Const("Hello, unknown person"),
        Button(Const("Useless button"), id="nothing"),
        state=st.newMavzu.name
    ) 
)






