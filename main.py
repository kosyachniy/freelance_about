"""
Telegram bot
"""

# Libraries
## System
import json

## External
from aiogram import Bot, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, \
                          InlineKeyboardButton, InlineKeyboardMarkup, \
                          ReplyKeyboardRemove, Message
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


async def echo_1(user):
    await send(
        user,
        """
Друзья здравствуйте!
Это наш бот, который расскажет о методе «Анкета Кристины Макаровой» ⛲

Расскажите, для чего вы здесь?
        """,
        (
            "Узнать о Методе",
            "Разборы с Кристиной",
            "Пройти Новую Терапию",
            "Мне все сразу",
        ),
    )

async def echo_2(user):
    await send(
        user,
        """
Анкета не была создана или придумана мною. Она пришла ко мне в состоянии пробуждения безмолвными вопросами, которые были обращены к обеспокоеному рядом со мной человеку. Находясь в переживании безмолвной истины о том, что в реальности беспокоиться не о чем, меня так удивило - что он о чем-то переживал.

Видя это, ко мне пришли вопросы, которые стали большим феноменом нашего времени в области психологии и самопознания. Феномен в том, что люди пытаются решать проблемы, которых не существует. Видение проблем создает наше эго - это совокупность подавленных болей, из которых вы состоите.

Если вы сейчас находитесь в состоянии тяжелых отношений, поисков самореализации, своей аутентичности, выхода из зависимости, одиночества, или попыткок принятия себя и своей самоценности  - Анкета станет невероятным открытием для вас и концом поисков, потому что после Анкеты вместе с проблемой исчезает и сам вопрос.

Я рада, что вы соприкоснетесь с Анкетой.
Анкета пришла ко мне 3 года назад и я делюсь ей совершенно бесплатно на своих встречах, у меня бесплатное консультирование по списку ожидания и для тех, кто хочет углубленно практиковать Анкету, появится возможность влиться в наше сообщество практиков, где более 70 человек проходят «Новую Терапию».

Также у нас есть сертификация консультантов метода Анкета, в наше сообщество вливается все больше профессиональных психотерапевтов с разных стран. Если вы работатее с людьми, на будещее обратите внимание на этот метод, он сократит годы вашей терапии и терапии ваших клиентов.

Ну что, готовы?
        """,
        (
            {'name': "Интересно!", 'type': 'callback', 'data': 'c1'},
        ),
        True,
    )

async def echo_3(user):
    await send(
        user,
        """
Давайте начнем!"

Что такое «Анкета»?"

Анкета - это вопросы, которые бы задал вам просветлённый человек, у которого нет тревог, который понимает истину. Особенность Анкеты в том, что она работает не с убеждениями, а с тем, что их создаёт.

Только правда исцеляет и суть Анкеты в том, что в реальности нет никаких проблем. Всё с вами в порядке. Всё правильно. Видение, что с нами или в мире что-то не так создаёт наш беспокойный ум. Мы держимся за эти беспокойства, думая что они реальны, но положив их на Анкету, вы увидите за каждым страхом пустоту.

Это «видение» проблем создаётся из нашей непрожитой боли. Когда с нами происходят травмирующие ситуации, мы подавляем в себе боль и потом весь мир видим сквозь нее. Так создаётся видение «чего-то»: через первичные травмы.

Травмы лишают нас понимания своего «да» и «нет». Из-за невозможности выразить себя и свои желания мы вынуждены подстраиваться, сомневаться в себе, обесценивать, вступать в нездоровые отношения или саботировать свое развитие.

Отсюда по цепочке вытекают все остальные проблемы в нашей жизни. Потому что когда мы не можем устроить свою жизнь и любить себя, мы будем нуждаться в других и злиться на мир, что он не может сделать это за нас. Так сложно прийти к внутреннему покою и чувствовать радость.

Анкета проводит к месту, где возникла эта боль и приглашает прожить. Когда вы проживаете, и сама проблема и видение её исчезает.

Вы увидите, что самое правильное и мудрое решение любой проблемы лежит вне вашего беспокойства. После проживания все становится ясно и вас отпускает. У вас остается безмолвное понимание вопроса, с которым пришли к Анкете. Вы откроете Мастера внутри себя.

Я каждый день работаю с людьми по Анкете, они приносят тысячи вопросов и с помощью Анкеты освобождаются от них.

Если вы готовы к правде, ресурсной и честной работе над собой, это поможет вам. Если вы не готовы к сдаче и снятию масок, Анкета вам не подойдет.

Но если вы к этому открыты, Анкета для вас 🌳
        """,
        (
            {'name': "Хочу практиковать!", 'type': 'callback', 'data': 'c2'},
        ),
        True,
    )

async def echo_4(user):
    await send(
        user,
        """
Здорово!

Чтобы начать работать по Анкете, послушайте эту аудиозапись, где я объясняю вопросы Анкеты и рассказываю о своей практике:

АУДИОФИАЙЛ (напиши емайл куда выслать аудиофайл для прикрепа?)

Скачайте саму Анкету здесь (файл ниже в пдф)

Посмотрите видео-работы здесь: https://www.youtube.com/channel/UCeTgZMycpmXmQnYHIjFB_PA (ссылку встроить в слово здесь)

Приходите на встречи со мной, чтобы задать свой вопрос, я спонтанно провожу их на канале «это не от этого» https://t.me/anketakm

Чтобы практиковать Анкету более углубленно и освободиться от своих травм и сценариев, приходите в Новую Терапию:
        """,
        (
            {'name': "Начать Новую Терапию", 'type': 'callback', 'data': 'c3'},
        ),
        True,
    )

async def echo_5(user):
    await send(
        user,
        """
Мы часто не осознаем своих травм и не понимаем, почему у нас возникают определенные проблемы в развитии, в личности, во взаимоотношениях, в сексуальности или проявлении себя в мире.

Программа «Новая Терапия» помогает увидеть все свои подавленности и с помощью группы практиков и партнера по работе экологично освобождаться от них параллельно со своей жизнью.

Эти 12 месяцев путешествия вглубь себя слой за слоем сначала снимают травмы с главными конфликтами в жизни и затем помогают понять свои аутентичные желания и наконец-то реализовать их в жизни. «Новая Терапия» мягко и кардинально трансформирует самоощущение и жизни участников программы.

Это лучшая программа по самопониманию, которую проходят участники из разных стран. Мы сделали доступной стоимость этой терапии - от 3000 рублей в месяц.

В программу входит:
Обучающая программа по Анкете
4 эфира с Кристиной в месяц
4 встречи с персональной командой
Работы в тандеме
Доступ в сообщество практиков

Вступайте в программу сейчас и получите бесплатную сессию с консультантом Анкеты!
ссылка
акция доступна до 29 мая (боту нужно подставлять дату которая будет на 3 дня вперед)
        """,
        (
            {'name': "Начать", 'type': 'link', 'data': 'https://my.8steps.live/newtherapy'},
        ),
        True,
    )

@dp.message_handler(commands=['start'])
async def handler_start(message: Message):
    await echo_1(message.chat.id)

@dp.message_handler(text="Узнать о Методе")
async def handler_more(message: Message):
    await echo_2(message.chat.id)

@dp.message_handler(text="Разборы с Кристиной")
async def handler_analysis(message: Message):
    await echo_3(message.chat.id)

@dp.message_handler(text="Пройти Новую Терапию")
async def handler_new(message: Message):
    await echo_4(message.chat.id)

@dp.message_handler(text="Мне все сразу")
async def handler_all(message: Message):
    await echo_5(message.chat.id)

@dp.callback_query_handler(lambda message: message.data == 'c1')
async def handler_c1(callback):
    await echo_3(callback.message.chat.id)

@dp.callback_query_handler(lambda message: message.data == 'c2')
async def handler_c1(callback):
    await echo_4(callback.message.chat.id)

@dp.callback_query_handler(lambda message: message.data == 'c3')
async def handler_c1(callback):
    await echo_5(callback.message.chat.id)

@dp.message_handler()
async def echo(message: Message):
    await echo_1(message.chat.id)

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
