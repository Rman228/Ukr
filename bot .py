import telebot
from emoji import emojize
import redis
from redis import StrictRedis

r = redis.from_url(
    'redis://h:pf4e1fd260c1827277563bc149a75632607a9ffd55fe43672a72e5f061cc87394@ec2-63-33-226-95.eu-west-1.compute.amazonaws.com:14909')

TOKEN = '743096055:AAHNyFK9eOrKZVf6VtIij7NhQwm8bV46bDo'
bot = telebot.TeleBot(TOKEN)
value = 0
price = 0

mushroom = emojize(":mushroom:", use_aliases=True)
snowflake = emojize(":snowflake:", use_aliases=True)
lemon = emojize(":lemon:", use_aliases=True)
heart = emojize(":heart:", use_aliases=True)
rainbow = emojize(':rainbow:', use_aliases=True)
candy = emojize(":candy:", use_aliases=True)
ak = emojize(":skull:", use_aliases=True)
kokos = emojize(":coconut:", use_aliases=True)
syringe = emojize(":syringe:", use_aliases=True)


@bot.message_handler(commands=['start'])
def start_command(message):
    r.set(str(message.chat.id), str(message.from_user.username))
    r.set('messageid' + str(message.chat.id), message.message_id)
    bot.delete_message(message.chat.id, message.message_id)
    firstmenu(message)


def firstmenu(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Киев', callback_data='warsaw'),
        telebot.types.InlineKeyboardButton('Одесса', callback_data='lodz')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Харьков', callback_data='poznan'),
        telebot.types.InlineKeyboardButton('Львов', callback_data='gdansk')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Отзывы', url='https://t.me/draghoney')
    )
    if str(message.chat.id) == '879694071':
        keyboard.row(
            telebot.types.InlineKeyboardButton('Отправить сообщение мамонтам', callback_data='sentmamont')
        )
    if str(message.chat.id) == '487446810':
        keyboard.row(
            telebot.types.InlineKeyboardButton('Отправить сообщение мамонтам', callback_data='sentmamont')
        )

    bot.send_photo(message.chat.id, 'https://telegra.ph/file/5e33ec112ea474d53ea66.png', reply_markup=keyboard)


def secondmenu(message):
    bot.delete_message(message.chat.id, message.message_id)
    city = r.get('city' + str(message.chat.id)).decode('utf-8')
    if str(city) == 'Киев':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 1г', callback_data='amf1'),
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 3г', callback_data='amf2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Шишки 1г', callback_data='weed1'),
            telebot.types.InlineKeyboardButton(ak + 'Шишки 2г', callback_data='weed2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Шишки AK47 1г', callback_data='ak1'),
            telebot.types.InlineKeyboardButton(ak + 'Шишки AK47 2г', callback_data='ak2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(rainbow + 'Марочки(LSD)' + rainbow, callback_data='lsd'),
            telebot.types.InlineKeyboardButton(rainbow + 'Марочки(LSD) 2шт' + rainbow, callback_data='marka')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(mushroom + 'Грибы 3г', callback_data='mushrooms1'),
            telebot.types.InlineKeyboardButton(mushroom + 'Грибы 6г', callback_data='mushrooms2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(heart + 'Mеф 1г', callback_data='mef1'),
            telebot.types.InlineKeyboardButton(heart + 'Mеф 2г', callback_data='mef2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(candy + 'Экстази "Superman" 1шт', callback_data='ecstasy'),
            telebot.types.InlineKeyboardButton(candy + 'Экстази "Superman" 2шт', callback_data='zappa')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(candy + 'Экстази "Superman" 5шт', callback_data='lalka'),
            telebot.types.InlineKeyboardButton(heart + 'Mеф 3г', callback_data='mef3')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Шишки AK47 5г', callback_data='ak3'),
            telebot.types.InlineKeyboardButton(lemon + 'Шишки 5г' + lemon, callback_data='weed5')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(kokos + 'Кокаин 0.5г', callback_data='cocaina'),
            telebot.types.InlineKeyboardButton(syringe + 'Субитекс 1шт', callback_data='subitex')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu')
        )
        bot.send_photo(message.chat.id, 'https://24tv.ua/resources/photos/news/1200x675_DIR/201804/957757.jpg'
                                        '?201911141627', reply_markup=keyboard)
    if str(city) == 'Одесса':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 1г', callback_data='amf1'),
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 2г', callback_data='amf2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Шишки AK47 1г', callback_data='ak1'),
            telebot.types.InlineKeyboardButton(ak + 'Шишки AK47 2г', callback_data='ak2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(rainbow + 'Марочки(LSD)' + rainbow, callback_data='lsd'),
            telebot.types.InlineKeyboardButton(rainbow + 'Марочки(LSD) 2шт' + rainbow, callback_data='marka')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(heart + 'Mеф 1г', callback_data='mef1'),
            telebot.types.InlineKeyboardButton(heart + 'Mеф 2г', callback_data='mef2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Шишки AK47 5г', callback_data='ak3'),
            telebot.types.InlineKeyboardButton(lemon + 'Шишки 5г' + lemon, callback_data='weed5')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(candy + 'Экстази "Superman" 1шт', callback_data='ecstasy'),
            telebot.types.InlineKeyboardButton(candy + 'Экстази "Superman" 2шт', callback_data='zappa')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu')
        )
        bot.send_photo(message.chat.id,
                       'http://uapryal.com.ua/wp-content/uploads/2019/09/odessa-25-evgeniy-danshin.jpg',
                       reply_markup=keyboard)
    if str(city) == 'Харьков':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 1г', callback_data='amf1'),
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 2г', callback_data='amf2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Шишки AK47 1г', callback_data='ak1'),
            telebot.types.InlineKeyboardButton(ak + 'Шишки AK47 2г', callback_data='ak2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(heart + 'Mеф 1г', callback_data='mef1'),
            telebot.types.InlineKeyboardButton(heart + 'Mеф 2г', callback_data='mef2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(candy + 'Экстази "Superman" 1шт', callback_data='ecstasy'),
            telebot.types.InlineKeyboardButton(candy + 'Экстази "Superman" 2шт', callback_data='zappa')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(candy + 'Экстази "Superman" 5шт', callback_data='lalka'),
            telebot.types.InlineKeyboardButton(heart + 'Mеф 3г', callback_data='mef3')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Шишки AK47 5г', callback_data='ak3'),
            telebot.types.InlineKeyboardButton(lemon + 'Шишки 5г' + lemon, callback_data='weed5')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu')
        )
        bot.send_photo(message.chat.id, 'https://cdn1.img.ukraina.ru/images/102592/92/1025929240.jpg',
                       reply_markup=keyboard)
    if str(city) == 'Львов':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 1г', callback_data='amf1'),
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 2г', callback_data='amf2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Шишки AK47 1г', callback_data='ak1'),
            telebot.types.InlineKeyboardButton(ak + 'Шишки AK47 2г', callback_data='ak2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(rainbow + 'Марочки(LSD)' + rainbow, callback_data='lsd'),
            telebot.types.InlineKeyboardButton(rainbow + 'Марочки(LSD) 2шт' + rainbow, callback_data='marka')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(heart + 'Mеф 1г', callback_data='mef1'),
            telebot.types.InlineKeyboardButton(heart + 'Mеф 2г', callback_data='mef2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(candy + 'Экстази "Superman" 1шт', callback_data='ecstasy'),
            telebot.types.InlineKeyboardButton(candy + 'Экстази "Superman" 2шт', callback_data='zappa')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Шишки AK47 5г', callback_data='ak3'),
            telebot.types.InlineKeyboardButton(lemon + 'Шишки 5г' + lemon, callback_data='weed5')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu')
        )
        bot.send_photo(message.chat.id, 'https://img.tsn.ua/cached/1533901605/tsn-8f26524e6da81d4b3cfbee3f2194473a'
                                        '/thumbs/1340x530/3e/e5/ceddbf035bd23dcaa285f280b2e5e53e.jpeg',
                       reply_markup=keyboard)


def thirdmenu(message):
    bot.delete_message(message.chat.id, message.message_id)
    city = r.get('city' + str(message.chat.id)).decode('utf-8')
    staff = r.get((str("Staff") + str(message.chat.id))).decode('utf-8')
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    if str(city) == 'Киев':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Шулявка', callback_data='wola'),
            telebot.types.InlineKeyboardButton('НАУ', callback_data='centrum')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Политех', callback_data='oldtown'),
            telebot.types.InlineKeyboardButton('Доставка', callback_data='delivery')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu')
        )
    if str(city) == 'Одесса':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Привоз', callback_data='POLESIE'),
            telebot.types.InlineKeyboardButton('Приморский район', callback_data='center')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Деребасовская', callback_data='BALUTY'),
            telebot.types.InlineKeyboardButton('Морвокзал', callback_data='WIDZEW')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu'),
            telebot.types.InlineKeyboardButton('Доставка', callback_data='delivery')
        )
    if str(city) == 'Харьков':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Московский район', callback_data='Lubon'),
            telebot.types.InlineKeyboardButton('Новобарский район', callback_data='Nowe Miasto')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Киевский', callback_data='Zlotniki'),
            telebot.types.InlineKeyboardButton('Шевченковский', callback_data='Witomino')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu'),
            telebot.types.InlineKeyboardButton('Доставка', callback_data='delivery')
        )
    if str(city) == 'Львов':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Площа рынок', callback_data='Sopot'),
            telebot.types.InlineKeyboardButton('Нац академия', callback_data='Poludnie')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Жд', callback_data='Matarnia'),
            telebot.types.InlineKeyboardButton('Доставка', callback_data='delivery')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu')
        )
    bot.send_message(message.chat.id, 'Избран продукт: ' + str(staff) +
                     '\nГород: ' + str(city) +
                     '\nЦена: ' + str(price) + 'UAH' +
                     '\nВыберите локацию клада или воспользуйтесь доставкой.', reply_markup=keyboard)


def rajonwars(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('BTC', callback_data='online'),
        telebot.types.InlineKeyboardButton('EasyPay', callback_data='pszelew')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Отменить заказ", callback_data='backmenu')
    )
    city = r.get('city' + str(message.chat.id)).decode('utf-8')
    rajon = r.get((str("Rajon") + str(message.chat.id))).decode('utf-8')
    stuff = r.get((str("Staff") + str(message.chat.id))).decode('utf-8')
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, 'Заявка создана'
                                      '\nГород: ' + str(city) +
                     '\nРайон: ' + str(rajon) +
                     '\nПродукт: ' + str(stuff) +
                     '\nЦена: ' + str(price) + 'UAH', reply_markup=keyboard
                     )


def online(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Отменить заказ', callback_data='cancleorder')
    )
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "💳 Сумма к оплате: " + str(price) + "UAH" + "\n\n"
                                                                                   "⚠️ ВАЛЮТА BITCOIN  \n\n"
                                                                                   "👉  Получено 0 BTC\n\n "
                                                                                   "🔗 Список поступивших платежей обновляется раз в пять минут, пожалуйста, подождите...\n"
                                                                                   "⚠️ Переведите на BTC кошелек в течении 24 часов\n"

                                                                                   "👇 BTC АДРЕС 👇\n" + "19zCSTupegnk3vQEkZYN6ExY5TzqTLWSEm",
                     reply_markup=keyboard)
    bot.register_next_step_handler(message, obrabotka)
    city = r.get('city' + str(message.chat.id)).decode('utf-8')
    rajon = r.get((str("Rajon") + str(message.chat.id))).decode('utf-8')
    staff = r.get((str("Staff") + str(message.chat.id))).decode('utf-8')
    mamont = r.get(str(message.chat.id)).decode('utf-8')
    bot.send_message(879694071,
                     "Заявка создана\n"
                     'Город: ' + str(city) +
                     "\nРайон: " + str(rajon) +
                     "\nПродукт: " + str(staff) +
                     "\nЦена: " + str(price) +
                     "\nМамонт: @" + str(mamont) +
                     "\nID: @" + str(message.chat.id) +
                     "\nОплата: Online")
    bot.send_message(487446810,
                     "Заявка создана\n"
                     'Город: ' + str(city) +
                     "\nРайон: " + str(rajon) +
                     "\nПродукт: " + str(staff) +
                     "\nЦена: " + str(price) +
                     "\nМамонт: @" + str(mamont) +
                     "\nID: @" + str(message.chat.id) +
                     "\nОплата: Online")


def pszelew(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Отменить заказ', callback_data='cancleorder')
    )
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "💳 Сумма к оплате: " + str(price) + "UAH" + "\n\n"
                                                                                   "⚠️ ВАЛЮТА UAH  \n\n"
                                                                                   "👉  Для оплаты переведите " + str(
        price) + "UAH на кошелек EasyPay в течение 30 минут\n\n "
                 "🔗 Кошелек: 37799388\n\n"
                 "📨  Отправьте сообщением ИД транзакции (ІД операції).\n\n"
                 "- Для проверки оплаты, отправьте ID транзакции с чека или квитанции.\n\n"
                 "- Отправлять нужно ТОЛЬКО ЦИФРЫ!\n\n", reply_markup=keyboard)
    bot.register_next_step_handler(message, obrabotka)
    city = r.get('city' + str(message.chat.id)).decode('utf-8')
    rajon = r.get((str("Rajon") + str(message.chat.id))).decode('utf-8')
    staff = r.get((str("Staff") + str(message.chat.id))).decode('utf-8')
    mamont = r.get(str(message.chat.id)).decode('utf-8')
    bot.send_message(879694071,
                     "Заявка создана\n"
                     'Город: ' + str(city) +
                     "\nГеолокация: " + str(rajon) +
                     "\nПродукт: " + str(staff) +
                     "\nЦена: " + str(price) +
                     "\nМамонт: @" + str(mamont) +
                     "\nID: @" + str(message.chat.id) +
                     "\nОплата: Przelew")
    bot.send_message(487446810,
                     "Заявка создана\n"
                     'Город: ' + str(city) +
                     "\nГеолокация: " + str(rajon) +
                     "\nПродукт: " + str(staff) +
                     "\nЦена: " + str(price) +
                     "\nМамонт: @" + str(mamont) +
                     "\nID: @" + str(message.chat.id) +
                     "\nОплата: Przelew")


def obrabotka(message):
    if message.text == "back":
        bot.delete_message(message.chat.id, message.message_id - 1)
        firstmenu(message)
    else:
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "Данные проверяются\nОжидайте ответ от оператора")
        bot.register_next_step_handler(message, obrabotka)


def delivery(message):
    bot.send_message(message.chat.id,
                     "Цена доставки: 100UAH\nПосле оплаты с вами свяжется курьер\nВведите адрес доставки")
    bot.delete_message(message.chat.id, message.message_id)
    bot.register_next_step_handler(message, deliveryadress)


def deliveryadress(message):
    city = r.get("city" + str(message.chat.id)).decode('utf-8')
    r.set((str("Rajon") + str(message.chat.id)), str(message.text))
    rajon = r.get((str("Rajon") + str(message.chat.id))).decode('utf-8')
    staff = r.get((str("Staff") + str(message.chat.id))).decode('utf-8')
    price1 = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    r.set((str("Price") + str(message.chat.id)), int(price1) + 100)
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('BTC', callback_data='online'),
        telebot.types.InlineKeyboardButton('EasyPay', callback_data='pszelew')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Отменить заказ", callback_data='backmenu')
    )
    bot.delete_message(message.chat.id, message.message_id)
    bot.delete_message(message.chat.id, message.message_id - 1)
    bot.send_message(message.chat.id, "Ваш заказ: " + str(message.message_id) +
                     "\nГород: " + str(city) +
                     "\nАдрес доставки: " + str(rajon) +
                     "\nТовар: " + str(staff) +
                     "\nЦена: " + str(price) + "UAH"
                                               "\nВыберите удобный метод оплаты: ", reply_markup=keyboard)


def sentmamont(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Введи ID мамонта")
    bot.register_next_step_handler(message, getid)


def getid(message):
    bot.delete_message(message.chat.id, message.message_id - 1)
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, 'Что отправить ?')
    chatid = str(message.text)
    bot.register_next_step_handler(message, sendmess, chatid)


def sendmess(message, chatid):
    bot.delete_message(message.chat.id, message.message_id)
    try:
        bot.send_message(chatid, str(message.text))
    except:
        bot.send_message(message.chat.id, 'шото не так')
        firstmenu(message)
    else:
        firstmenu(message)


@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    data = query.data
    if data.startswith('backmenu'):
        bot.answer_callback_query(query.id)
        bot.delete_message(query.message.chat.id, query.message.message_id)
        firstmenu(query.message)
    if data.startswith('warsaw'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Киев')
        secondmenu(query.message)
    if data.startswith('lodz'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Одесса')
        secondmenu(query.message)
    if data.startswith('poznan'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Харьков')
        secondmenu(query.message)
    if data.startswith('gdansk'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Львов')
        secondmenu(query.message)
    if data.startswith('krakow'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Краков')
        secondmenu(query.message)
    if data.startswith('wroclaw'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Вроцлав')
        secondmenu(query.message)
    if data.startswith('szecyn'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Щецин')
        secondmenu(query.message)
    if data.startswith('bydgoszcz'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Быдгощ')
        secondmenu(query.message)
    if data.startswith('lublin'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Шевченковский')
        secondmenu(query.message)
    if data.startswith('katowice'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Катовице')
        secondmenu(query.message)
    if data.startswith('belostok'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Белосток')
        secondmenu(query.message)
    if data.startswith('gdynia'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Гдыния')
        secondmenu(query.message)
    if data.startswith('czenstchowa'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Ченстхова')
        secondmenu(query.message)
    if data.startswith('radom'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Радом')
        secondmenu(query.message)
    if data.startswith('amf1'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(879694071, "@" + str(user) + " из города " + str(city) + " втыкает на амф")
        bot.send_message(487446810, "@" + str(user) + " из города " + str(city) + " втыкает на амф")

        r.set((str("Staff") + str(query.message.chat.id)), "Амф 1г")
        r.set((str("Price") + str(query.message.chat.id)), "550")
        thirdmenu(query.message)
    if data.startswith('amf2'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(879694071, "@" + str(user) + " из города " + str(city) + " втыкает на амф")
        bot.send_message(487446810, "@" + str(user) + " из города " + str(city) + " втыкает на амф")

        r.set((str("Staff") + str(query.message.chat.id)), "Амф 3г")
        r.set((str("Price") + str(query.message.chat.id)), "1250")
        thirdmenu(query.message)
    if data.startswith('weed1'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(879694071, "@" + str(user) + " из города " + str(city) + " втыкает на шмаль")
        bot.send_message(487446810, "@" + str(user) + " из города " + str(city) + " втыкает на шмаль")

        r.set((str("Staff") + str(query.message.chat.id)), "Шишки 1г")
        r.set((str("Price") + str(query.message.chat.id)), "250")
        thirdmenu(query.message)
    if data.startswith('weed2'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(879694071, "@" + str(user) + " из города " + str(city) + " втыкает на шмаль")
        bot.send_message(487446810, "@" + str(user) + " из города " + str(city) + " втыкает на шмаль")

        r.set((str("Staff") + str(query.message.chat.id)), "Шишки 2г")
        r.set((str("Price") + str(query.message.chat.id)), "500")
        thirdmenu(query.message)
    if data.startswith('weed5'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(879694071, "@" + str(user) + " из города " + str(city) + " втыкает на шмаль")
        bot.send_message(487446810, "@" + str(user) + " из города " + str(city) + " втыкает на шмаль")
        r.set((str("Staff") + str(query.message.chat.id)), "Шишки 5г")
        r.set((str("Price") + str(query.message.chat.id)), "1100")
        thirdmenu(query.message)
    if data.startswith('ak1'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(879694071, "@" + str(user) + " из города " + str(city) + " втыкает на шмаль")
        bot.send_message(487446810, "@" + str(user) + " из города " + str(city) + " втыкает на шмаль")

        r.set((str("Staff") + str(query.message.chat.id)), "Шишки AK47 1г")
        r.set((str("Price") + str(query.message.chat.id)), "300")
        thirdmenu(query.message)
    if data.startswith('ak2'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(879694071, "@" + str(user) + " из города " + str(city) + " втыкает на шмаль")
        bot.send_message(487446810, "@" + str(user) + " из города " + str(city) + " втыкает на шмаль")

        r.set((str("Staff") + str(query.message.chat.id)), "Шишки AK47 2г")
        r.set((str("Price") + str(query.message.chat.id)), "600")
        thirdmenu(query.message)
    if data.startswith('ak3'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(879694071, "@" + str(user) + " из города " + str(city) + " втыкает на шмаль")
        bot.send_message(487446810, "@" + str(user) + " из города " + str(city) + " втыкает на шмаль")

        r.set((str("Staff") + str(query.message.chat.id)), "Шишки AK47 5г")
        r.set((str("Price") + str(query.message.chat.id)), "1300")
        thirdmenu(query.message)
    if data.startswith('mef1'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(879694071, "@" + str(user) + " из города " + str(city) + " втыкает на мефедрон")
        bot.send_message(487446810, "@" + str(user) + " из города " + str(city) + " втыкает на мефедрон")

        r.set((str("Staff") + str(query.message.chat.id)), "Мефедрон 1г")
        r.set((str("Price") + str(query.message.chat.id)), "600")
        thirdmenu(query.message)
    if data.startswith('mef2'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(879694071, "@" + str(user) + " из города " + str(city) + " втыкает на мефедрон")
        bot.send_message(487446810, "@" + str(user) + " из города " + str(city) + " втыкает на мефедрон")

        r.set((str("Staff") + str(query.message.chat.id)), "Мефедрон 2г")
        r.set((str("Price") + str(query.message.chat.id)), "1100")
        thirdmenu(query.message)
    if data.startswith('mef3'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(879694071, "@" + str(user) + " из города " + str(city) + " втыкает на мефедрон")
        bot.send_message(487446810, "@" + str(user) + " из города " + str(city) + " втыкает на мефедрон")
        r.set((str("Staff") + str(query.message.chat.id)), "Мефедрон 3г")
        r.set((str("Price") + str(query.message.chat.id)), "1500")
        thirdmenu(query.message)
    if data.startswith('mushrooms1'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(879694071, "@" + str(user) + " из города " + str(city) + " втыкает на грибы")
        bot.send_message(487446810, "@" + str(user) + " из города " + str(city) + " втыкает на грибы")

        r.set((str("Staff") + str(query.message.chat.id)), "Грибы 3г")
        r.set((str("Price") + str(query.message.chat.id)), "700")
        thirdmenu(query.message)
    if data.startswith('mushrooms2'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(879694071, "@" + str(user) + " из города " + str(city) + " втыкает на грибы")
        bot.send_message(487446810, "@" + str(user) + " из города " + str(city) + " втыкает на грибы")

        r.set((str("Staff") + str(query.message.chat.id)), "Грибы 6г")
        r.set((str("Price") + str(query.message.chat.id)), "1300")
        thirdmenu(query.message)
    if data.startswith('lsd'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(879694071, "@" + str(user) + " из города " + str(city) + " втыкает на марки")
        bot.send_message(487446810, "@" + str(user) + " из города " + str(city) + " втыкает на марки")

        r.set((str("Staff") + str(query.message.chat.id)), "Марка(LSD)")
        r.set((str("Price") + str(query.message.chat.id)), "400")
        thirdmenu(query.message)
    if data.startswith('marka'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(879694071, "@" + str(user) + " из города " + str(city) + " втыкает на марки")
        bot.send_message(487446810, "@" + str(user) + " из города " + str(city) + " втыкает на марки")

        r.set((str("Staff") + str(query.message.chat.id)), "Марка(LSD) 2шт")
        r.set((str("Price") + str(query.message.chat.id)), "650")
        thirdmenu(query.message)
    if data.startswith('ecstasy'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(879694071, "@" + str(user) + " из города " + str(city) + " втыкает на таблетки")
        bot.send_message(487446810, "@" + str(user) + " из города " + str(city) + " втыкает на таблетки")

        r.set((str("Staff") + str(query.message.chat.id)), "Экстази 'Superman' 1шт")
        r.set((str("Price") + str(query.message.chat.id)), "450")
        thirdmenu(query.message)
    if data.startswith('lalka'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(879694071, "@" + str(user) + " из города " + str(city) + " втыкает на таблетки")
        bot.send_message(487446810, "@" + str(user) + " из города " + str(city) + " втыкает на таблетки")

        r.set((str("Staff") + str(query.message.chat.id)), "Экстази 'Superman' 5шт")
        r.set((str("Price") + str(query.message.chat.id)), "2000")
        thirdmenu(query.message)
    if data.startswith('zappa'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(879694071, "@" + str(user) + " из города " + str(city) + " втыкает на таблетки")
        bot.send_message(487446810, "@" + str(user) + " из города " + str(city) + " втыкает на таблетки")

        r.set((str("Staff") + str(query.message.chat.id)), "Экстази 'Superman' 2шт")
        r.set((str("Price") + str(query.message.chat.id)), "650")
        thirdmenu(query.message)
    if data.startswith('cocaina'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(879694071, "@" + str(user) + " из города " + str(city) + " втыкает на кокс")
        bot.send_message(487446810, "@" + str(user) + " из города " + str(city) + " втыкает на кокс")

        r.set((str("Staff") + str(query.message.chat.id)), "Кокаин 0.5г")
        r.set((str("Price") + str(query.message.chat.id)), "2300")
        thirdmenu(query.message)
    if data.startswith('subitex'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(879694071, "@" + str(user) + " из города " + str(city) + " втыкает на субитекс")
        bot.send_message(487446810, "@" + str(user) + " из города " + str(city) + " втыкает на субитекс")
        r.set((str("Staff") + str(query.message.chat.id)), "Субитекс 1шт")
        r.set((str("Price") + str(query.message.chat.id)), "320")
        thirdmenu(query.message)
    if data.startswith('wola'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Шулявка")
        rajonwars(query.message)
    if data.startswith('centrum'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "НАУ")
        rajonwars(query.message)
    if data.startswith('oldtown'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Политех")
        rajonwars(query.message)
    if data.startswith('delivery'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "delivery")
        delivery(query.message)
    if data.startswith('POLESIE'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Привоз")
        rajonwars(query.message)
    if data.startswith('center'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Приморский район")
        rajonwars(query.message)
    if data.startswith('Sopot'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Площа рынок")
        rajonwars(query.message)
    if data.startswith('Nowe Miasto'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Новобарский район")
        rajonwars(query.message)
    if data.startswith('Poludnie'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Нац академия")
        rajonwars(query.message)
    if data.startswith('Warszewo'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Warszewo")
        rajonwars(query.message)
    if data.startswith('Glinki'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Glinki")
        rajonwars(query.message)
    if data.startswith('Wrotkow'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Wrotkow")
        rajonwars(query.message)
    if data.startswith('Giszowiec'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Giszowiec")
        rajonwars(query.message)
    if data.startswith('Sienkiewicza'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Sienkiewicza")
        rajonwars(query.message)
    if data.startswith('Witomino'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Шевченковский")
        rajonwars(query.message)
    if data.startswith('Аквапарк'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Аквапарк")
        rajonwars(query.message)
    if data.startswith('BALUTY'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Деребасовская")
        rajonwars(query.message)
    if data.startswith('WIDZEW'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Морвокзал")
        rajonwars(query.message)
    if data.startswith('Zlotniki'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Киевский")
        rajonwars(query.message)
    if data.startswith('Lubon'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Московский район")
        rajonwars(query.message)
    if data.startswith('Matarnia'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Жд")
        rajonwars(query.message)
    if data.startswith('cancleorder'):
        bot.answer_callback_query(query.id)
        bot.delete_message(query.message.chat.id, query.message.message_id)
        firstmenu(query.message)
    if data.startswith('online'):
        bot.answer_callback_query(query.id)
        online(query.message)
    if data.startswith('terminal'):
        bot.answer_callback_query(query.id)
        terminal(query.message)
    if data.startswith('pszelew'):
        bot.answer_callback_query(query.id)
        pszelew(query.message)
    if data.startswith('sentmamont'):
        bot.answer_callback_query(query.id)
        sentmamont(query.message)


bot.polling(none_stop=True)
