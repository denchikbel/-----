from aiogram.types import KeyboardButton,Message,ReplyKeyboardMarkup
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU
from aiogram import Router
from aiogram.utils.keyboard import ReplyKeyboardBuilder

kb_bulder=ReplyKeyboardBuilder()
coon = KeyboardButton( text='отправить телефон',
                          request_contact=True
                          )
kb_bulder.row(coon)
keyboard: ReplyKeyboardMarkup = kb_bulder.as_markup(resize_keyboard=True)

router:Router = Router()
# хендлер на команду старт
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'])

# хендлер на команду хелп
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=keyboard)