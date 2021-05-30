"""
Telegram bot
"""

# Libraries
## System
import json

## External
from aiogram import Bot, types
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardRemove, \
                          ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook


# Params
with open('sets.json', 'r') as file:
    sets = json.loads(file.read())
    WEBHOOK_URL = sets['tg']['server']

with open('keys.json', 'r') as file:
    keys = json.loads(file.read())
    TG_TOKEN = keys['tg']['token']

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = 8101 # TODO: 80


# Global variables
bot = Bot(token=TG_TOKEN)
dp = Dispatcher(bot)


# Funcs
def keyboard(rows, inline=False):
	if rows == []:
		if inline:
			return InlineKeyboardMarkup()
		else:
			return ReplyKeyboardRemove()

	if rows in (None, [], [[]]):
		return rows

	if inline:
		buttons = InlineKeyboardMarkup()
	else:
		buttons = ReplyKeyboardMarkup(resize_keyboard=True)

	if type(rows[0]) not in (list, tuple):
		rows = [[button] for button in rows]

	for cols in rows:
		if inline:
			buttons.add(*[InlineKeyboardButton(col['name'], **({'url': col['data']} if col['type'] == 'link' else {'callback_data': col['data']})) for col in cols])
		else:
			buttons.add(*[KeyboardButton(col) for col in cols])

	return buttons

## Send message
async def send(user, text='', buttons=None, inline=False, image=None, preview=False):
	if not image:
		return await bot.send_message(
			user,
			text,
			reply_markup=keyboard(buttons, inline),
			disable_web_page_preview=not preview,
		)

	else:
		return await bot.send_photo(
			user,
			image,
			text,
			reply_markup=keyboard(buttons, inline),
		)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    # return SendMessage
    await send(
        message.chat.id,
        """Друзья здравствуйте!"""
        """\nЭто наш бот, который расскажет о методе «Анкета Кристины Макаровой» ⛲"""
        """\n"""
        """\nРасскажите, для чего вы здесь?""",
        (
            "Узнать о Методе",
            "Разборы с Кристиной",
            "Пройти Новую Терапию",
            "Мне все сразу",
        ),
    )

@dp.message_handler()
async def echo(message: types.Message):
    """ Main handler """

    await bot.send_message(message.chat.id, message.text)


async def on_start(x):
    """ Handler on the bot start """

    await bot.set_webhook(WEBHOOK_URL)

    # # Actions after start

# async def on_stop(dp):
#     """ Handler on the bot stop """

#     # # Actions before shutdown

#     # Remove webhook (not acceptable in some cases)
#     await bot.delete_webhook()

#     # Close DB connection (if used)
#     await dp.storage.close()
#     await dp.storage.wait_closed()


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path='',
        on_startup=on_start,
        # on_shutdown=on_stop,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
