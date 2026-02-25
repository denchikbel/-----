import asyncio
import logging
from aiogram import Bot, Dispatcher
from config.config import Config, load_config
from handlers import user, other
#для кнопок 



#функция конфигурирования и запуска бота
async def main()-> None:
    #загружаем конфиг в перменную
    config: Config = load_config()
    logging.basicConfig(
        level=logging.getLevelName(level=config.log.level),
        format=config.log.format
    )

    bot = Bot(token = config.bot.token)
    dp: Dispatcher = Dispatcher()

    # регистрируем роутеры в диспетчере
    dp.include_router(user.router)
    dp.include_router(other.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
    

asyncio.run(main())