from config  import TELEGRAM_TOKEN
from aiogram import Bot, Dispatcher, types
from asyncio import run
from logging import basicConfig, INFO
from sys     import stdout

from aiogram.enums   import ParseMode
from aiogram.filters import CommandStart

bot = Bot(TELEGRAM_TOKEN, parse_mode=ParseMode.HTML)
dp  = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    """
    Обработчик команды /start
    :param message: Message: Сообщение пользователя
    :return:                 None
    """
    await bot.send_message(
        message.chat.id,
        text='Отправь сообщение боту!',
    )


@dp.message()
async def message_handler(message: types.Message) -> None:
    """
    Обработчик сообщений от пользователя
    :param message: Message: Сообщение пользователя
    :return:                 None
    """
    await message.answer(
        text=f'Вы сказали: {message.text}'
    )


async def main() -> None:
    """
    Главная функция для запуска бота
    :return: None
    """
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        basicConfig(level=INFO, stream=stdout)
        run(main())

    except KeyboardInterrupt:
        print('The bot has successfully completed its work!')
