from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU

# хендлер на команду старт
@dp.message(CommandStart)
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'])

# хендлер на команду хелп
@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])