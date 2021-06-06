"""
Telegram bot
"""

# Libraries
## System
import json
import datetime
from collections import defaultdict

## External
from aiogram import Bot, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, \
                          InlineKeyboardButton, InlineKeyboardMarkup, \
                          ReplyKeyboardRemove, Message
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook

## Local
from mongodb import db


# Params
with open('sets.json', 'r') as file:
    sets = json.loads(file.read())
    WEBHOOK_URL = sets['tg']['server']
    ADMINS = sets['admins']

with open('keys.json', 'r') as file:
    keys = json.loads(file.read())
    TG_TOKEN = keys['tg']['token']

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = 8101 # TODO: 80


# Global variables
bot = Bot(token=TG_TOKEN)
dp = Dispatcher(bot)


# Funcs
def keyboard(user, rows, inline=False):
	if rows == []:
		if inline:
			return InlineKeyboardMarkup()
		else:
			return ReplyKeyboardRemove()

	if rows in (None, [], [[]]):
		return rows

	if not inline and user in ADMINS:
		rows = list(rows) + ['Статистика']

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
async def send(user, text='', buttons=None, inline=False, image=None, preview=False, markup=None):
	if not image:
		return await bot.send_message(
			user,
			text,
			reply_markup=keyboard(user, buttons, inline),
			parse_mode=markup,
			disable_web_page_preview=not preview,
		)

	else:
		return await bot.send_photo(
			user,
			image,
			text,
			reply_markup=keyboard(user, buttons, inline),
			parse_mode=markup,
		)

async def send_file(user, name):
	with open(name, 'rb') as file:
		return await bot.send_document(user, file)


async def echo_1(user):
    await send(
        user,
        """
Друзья, здравствуйте!
Это наш бот, который расскажет о методе «Анкета Кристины Макаровой» ⛲

Расскажите, для чего вы здесь?
        """,
        (
            "Узнать о Методе",
            "Разборы с Кристиной",
            "Пройти Новую Терапию",
        ),
    )

async def echo_2(user):
    await send(
        user,
        """
Анкета не была создана или придумана мною.

Она пришла ко мне в состоянии пробуждения безмолвными вопросами, которые были обращены к обеспокоенному рядом со мной человеку. Находясь в переживании кристально чистой истины о том, что в реальности беспокоиться не о чем, меня удивило, что он о чем-то переживал.

Так пришли эти вопросы Анкеты и стали большим феноменом нашего времени в области психологии и самопознания. Феномен в том, что люди пытаются решать проблемы, которых не существует. Видение проблем и беспокойств создает наше эго, а это – совокупность подавленных болей, из которых вы состоите.

Если вы сейчас находитесь:
▫️ в состоянии тяжелых отношений, поисках самореализации, своей аутентичности
▫️ выхода из зависимости, апатии, синдрома невидимки
▫️ хотите понять себя, открыться и чувствовать самоценность – Анкета станет невероятным открытием для вас и концом поисков, потому что после Анкеты вместе с проблемой исчезает и сам вопрос.

Я рада, что вы соприкоснетесь с Анкетой. Анкета пришла ко мне 3 года назад и я делюсь ей совершенно бесплатно на своих встречах, у меня бесплатное консультирование по списку ожидания и для тех, кто хочет углубленно практиковать Анкету, есть возможность присоединиться  в наше сообщество практиков, где более 70 человек проходят «Новую Терапию».

Также у нас есть сертификация консультантов метода «Анкета», в нашем сообществе становится все больше профессиональных психотерапевтов с разных стран.

Если вы работаете с людьми, обратите внимание на этот метод, он сократит годы вашей терапии и терапии ваших клиентов.

▫️ [Новая Терапия](http://anketa.live/new_therapy)
▫️ [Сертификация](http://anketa.live/certfy)

Ну что, готовы?
        """,
        (
            {'name': "Интересно!", 'type': 'callback', 'data': 'c1'},
        ),
        True,
        markup='Markdown',
    )

async def echo_3(user):
    await send(
        user,
        """
Давайте начнем!

Что такое «Анкета»?

Анкета - это вопросы, которые бы задал вам просветлённый человек, свободный от тревог и понимающий истину. Особенность Анкеты в том, что она работает не с убеждениями и проблемами, а с тем, что их создаёт.

Только правда исцеляет и суть Анкеты в том, что в реальности нет никаких проблем. Всё с вами в порядке. Всё правильно.

Видение, что с нами или в мире что-то не так создаёт наш беспокойный ум. Мы держимся за эти беспокойства, думая что они реальны, но положив их на Анкету, вы увидите за каждым страхом пустоту.

«Видение» проблем создаётся из нашей непрожитой боли. Когда с нами происходят травмирующие ситуации, мы подавляем в себе боль и потом весь мир видим сквозь нее.

Травмы лишают нас понимания своего «да» и «нет». Из-за невозможности выразить себя и свои желания мы вынуждены подстраиваться, сомневаться в себе, обесценивать, вступать в нездоровые отношения или саботировать свое развитие. Отсюда по цепочке вытекают все остальные проблемы в нашей жизни.

Потому что когда мы не можем любить себя и устроить свою жизнь так, как хотим, мы будем нуждаться в других и злиться на мир, что он не может сделать это за нас. Так сложно прийти к внутреннему покою и чувствовать радость.

Анкета проводит к месту, где возникла эта боль и приглашает прожить ее. Когда вы проживаете, и сама проблема и видение её исчезает.

Вы увидите, что самое правильное и мудрое решение любой проблемы лежит вне вашего беспокойства. Любое беспокойство с Анкетой растворяется и после проживания остается лишь свобода и безмолвное понимание вопроса, с которым пришли к Анкете. Так раскрывается Мастера внутри вас.

Я каждый день работаю с людьми по Анкете, они приносят тысячи вопросов и с помощью Анкеты освобождаются от них. И это удивительный процесс, расставляющий все на свои места.

Если вы готовы к правде, ресурсной и честной работе над собой, это поможет вам. Если вы не готовы к сдаче и снятию масок, Анкета вам не подойдет.

Если вы к этому открыты, Анкета для вас 🌳

▫️ [Разборы с Кристиной](https://t.me/anketakm/113)
▫️ [Статьи о природе беспокойств](https://instagram.com/_kristinamakarova)
        """,
        (
            {'name': "Хочу практиковать!", 'type': 'callback', 'data': 'c2'},
        ),
        True,
        markup='Markdown',
    )

async def echo_4(user):
    await send(
        user,
        """
Чтобы начать работать по Анкете, послушайте эту аудиозапись, где я объясняю вопросы Анкеты и рассказываю о своей практике:
        """,
        (
            "Узнать о Методе",
            "Разборы с Кристиной",
            "Пройти Новую Терапию",
        ),
    )

    await send_file(
        user,
        'Как работать по Анкете КМ.mp3',
    )

    await send_file(
        user,
        'Анкета Кристины Макаровой.pdf',
    )

    await send(
        user,
        """
▫️ Скачайте саму Анкету

▫️ Посмотрите [видео-работы](https://www.youtube.com/channel/UCeTgZMycpmXmQnYHIjFB_PA)

▫️ Приходите на встречи со мной, чтобы задать свой вопрос. Я спонтанно провожу их на канале [«это не от этого»](https://t.me/anketakm)

▫️ Чтобы практиковать Анкету более углубленно и освободиться от своих травм и сценариев, приходите в [Новую Терапию](http://anketa.live/new_therapy)
        """,
        (
            {'name': "Начать Новую Терапию", 'type': 'callback', 'data': 'c3'},
        ),
        True,
        markup='Markdown',
    )

async def echo_5(user):
    MONTHS = (
        'января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
        'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря',
    )

    date = datetime.datetime.now() + datetime.timedelta(days=3)
    date_text = f"{date.day} {MONTHS[date.month-1]}"

    await send(
        user,
        f"""
Мы часто не осознаем своих травм и не понимаем причин, почему у нас возникают определенные проблемы в развитии, в личности, во взаимоотношениях, в сексуальности или проявлении себя в мире.

Программа «Новая Терапия» помогает увидеть все свои подавленные чувства и с помощью группы практиков и партнера по работе экологично освободиться от них.

«Новая Терапия» мягко и кардинально трансформирует самоощущение и жизни участников программы из разных стран.

Эти 12 месяцев путешествия вглубь себя слой за слоем сначала снимают травмы с главными конфликтами в жизни и затем помогают понять свои аутентичные желания и наконец-то реализовать их в жизни.

Жизнь радостна, когда вы открыты и можете делать что вы хотите, без барьеров.

Это лучшая программа по самопониманию, я от сердца рекомендую всем, кто хочет решить свои проблемы и жить в ладу с собой.

В программу входит:
Обучающая программа по Анкете
4 эфира с Кристиной в месяц
4 встречи с персональной командой
Работы в тандеме
Доступ в сообщество практиков

Мы сделали доступной стоимость этой терапии - от 3000 рублей в месяц.

Вступайте в программу сейчас и получите сессию с консультантом Анкеты в подарок!
Подробнее здесь:
https://my.8steps.live/newtherapy

Предложение действует только до {date_text}
        """,
        (
            {'name': "Начать", 'type': 'link', 'data': 'https://my.8steps.live/newtherapy'},
        ),
        True,
    )

async def echo_stat(to_user):
    if to_user not in ADMINS:
        return

    users = list(db['users'].find({}, {'_id': False, 'source': True}))
    count = len(users)
    text = f"Всего: {count}\n\nПереходы по источникам:\n"

    if not count:
        return

    sources = defaultdict(int)
    for user in users:
        sources[user['source']] += 1

    for source in sources:
        if source:
            source_name = source
        else:
            source_name = 'Пришли сами'

        text += f"\n{source_name}: {sources[source]} чел. ({round(sources[source]*100/count, 1)}%)"

    # Buttons stat

    c1 = len(set(db.sys.find_one({'name': 'c1'}, {'_id': False, 'cont': True})['cont']))
    c2 = len(set(db.sys.find_one({'name': 'c2'}, {'_id': False, 'cont': True})['cont']))
    c3 = len(set(db.sys.find_one({'name': 'c3'}, {'_id': False, 'cont': True})['cont']))

    text += f"\n\nПереходы по кнопкам:\n" \
            f"\nИнтересно! — {c1}" \
            f"\nХочу практиковать! — {c2}" \
            f"\nНачать Новую Терапию — {c3}"

    #

    await send(
        to_user,
        text,
        (
            "Узнать о Методе",
            "Разборы с Кристиной",
            "Пройти Новую Терапию",
        ),
    )

@dp.message_handler(commands=['start'])
async def handler_start(message: Message):
    try:
        source = message.text.split()[1]
    except:
        source = None

    user = db['users'].find_one({'id': message.from_user.id}, {'_id': True})

    if not user:
        db['users'].insert_one({
            'id': message.from_user.id,
            'login': message.from_user.username,
            'source': source,
            'created': datetime.datetime.now(),
        })

    await echo_1(message.chat.id)

@dp.message_handler(text="Узнать о Методе")
async def handler_more(message: Message):
    await echo_2(message.chat.id)

@dp.message_handler(text="Разборы с Кристиной")
async def handler_analysis(message: Message):
    await echo_3(message.chat.id)

@dp.message_handler(text="Пройти Новую Терапию")
async def handler_new(message: Message):
    await echo_5(message.chat.id)

@dp.message_handler(text="Статистика")
async def handler_stat(message: Message):
    await echo_stat(message.chat.id)

@dp.callback_query_handler(lambda message: message.data == 'c1')
async def handler_c1(callback):
    user_id = callback.message.chat.id
    db.sys.update_one({'name': 'c1'}, {'$push': {'cont': user_id}})
    await echo_3(user_id)

@dp.callback_query_handler(lambda message: message.data == 'c2')
async def handler_c1(callback):
    user_id = callback.message.chat.id
    db.sys.update_one({'name': 'c2'}, {'$push': {'cont': user_id}})
    await echo_4(user_id)

@dp.callback_query_handler(lambda message: message.data == 'c3')
async def handler_c1(callback):
    user_id = callback.message.chat.id
    db.sys.update_one({'name': 'c3'}, {'$push': {'cont': user_id}})
    await echo_5(user_id)

@dp.message_handler()
async def echo(message: Message):
    if message.chat.id in ADMINS:
        db_condition = {'id': {'$ne': message.chat.id}}
        db_filter = {'_id': False, 'id': True}
        for user in db['users'].find(db_condition, db_filter):
            await send(user['id'], message.text)

        await send(message.chat.id, "Отправлено всем!")

    else:
        text = f"Сообщение от {message.from_user.first_name} {message.from_user.last_name}"
        if message.chat.username:
            text += f" (@{message.from_user.username})"
        text += ":\n\n" + message.text

        for user in ADMINS:
            try:
               await send(user, text)
            except:
                pass

        await send(message.chat.id, "Ваш отзыв отправлен!")

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
