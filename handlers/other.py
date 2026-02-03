from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU


#хендлер на любые сообщения кроме хелп и старт
@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        message.reply(text=LEXICON_RU['no_echo'])
