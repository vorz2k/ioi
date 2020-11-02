import locale

from django.core.management.base import BaseCommand
import telebot
from . import dbworker
from telebot import types 
from ...models import User, settings_bot
from django.utils import translation
from ...utils import set_idis, get_user, set_1, get_idis, get_feedback, get_nextfee, godemode, set_2, token, set_3, set_4, set_5, up, get_vk
from pprint import pprint
from datetime import *
import json
from SimpleQIWI import *
#from block_io import BlockIo

selidd = {}
sels = 0
seld = {}
twrdd = {}
twrs = 0
twrd = {}
class Command(BaseCommand):

    help = 'Телеграм-бот'

    def handle(self, *args, **options):
        name = 'karel'
        tok = token(name, update=True)
        bot = telebot.TeleBot(str(tok.token_bot))
        us = '79169741812' # Номер телефона с семеркой но без +
        TOK = '4dfc2e4ea96775a9c6c19aa218be578b' # токен киви
        api = QApi(token=TOK, phone=us)
        version = 2 # API version
        #block_io = BlockIo('44a5-4ad3-6d84-4255', 'accauntClash1200', version)
        #print (block_io.get_balance())
        print(bot.get_me())
        """
        Набор функция для бота
        :param bot: Объект телеграм бота
        """
        dbworker.set_state(str(713832075) + 'diogram', 1)
        dbworker.set_state(str(713832075) + '_gl_admin', 5)
        #dbworker.set_stat('registered_users', str(713832075))
        moderator_group_id = "-1001323331539"
        worker_group_id = "-1001182459169"
        dbworker.set_state(str(moderator_group_id) + '_gl_admin', 5)
        dbworker.set_state(str(worker_group_id) + '_wrkr', 1)
        dbworker.set_state(str(worker_group_id) + '_status', 2)
        dbworker.set_state(str(713832075) + '_status', 2)
        #dbworker.set_state(str(713832075) + '_obl', 0)
        user_data = {}
        buf2 = []
        class User:
            def __init__(self, ms):
                self.ms = ms
        sels = 0
        seld = {}
        selidd = {}
        dbworker.set_state('sels', str(sels + 1))
        def afterclear():
            global sels, seld, selidd
            sels = 0
            seld = {}
            selidd = {}
            dbworker.set_stat('selidd', json.dumps(selidd))
            dbworker.set_stat('sels', int(sels))
            dbworker.set_stat('seld', json.dumps(seld))
            selidd = json.loads(dbworker.get_state('selidd'))
            sels = int(dbworker.get_stat('sels'))
            seld = json.loads(dbworker.get_stat('seld'))
        @bot.message_handler(commands=['diogram'])
        def ban(message):
            if dbworker.get_state(str(moderator_group_id) + '_gl_admin') == '5':
                bot.send_message(moderator_group_id, 'Статистика:\nПользователей: <b>' + str(dbworker.get_state(str(message.chat.id) + 'diogram')) + '</b>',parse_mode="Html")
            else:
                bot.send_message(message.chat.id, '❌ Вы не обладаете правами админа!')
        @bot.message_handler(commands=['gprime'])
        def give_prime(message):
            idis = message.text.split()[1]
            o = str(message.text.split()[2])
            user = set_idis(message, update=True)
            bot.send_message(idis, '❤️ Поздравляем, вы получаете прайм статус')
            bot.send_message(message.chat.id, '❤️ Команда выполнена успешно.')
        @bot.message_handler(commands=['rank'])
        def rank(message, update=False):
            if dbworker.get_state(str(message.chat.id) + '_gl_admin') == '5':
                
                #user = idis(message, update=True)
                try:
                    idis = message.text.split()[1]
                    print(idis)
                    o = str(message.text.split()[2])
                    print(o)
                    user = get_idis(message, update=True)
                    if o == '1':
                        users = get_user(message, update=True)
                        user = get_idis(message, update=True)
                        dbworker.set_state(str(idis) + '_gl_admin', int(o))
                        bot.send_message(idis, '⛔ Вы заблокированны на данном сервисе ⛔')
                        
                    elif o == '2':
                        dbworker.set_state(str(idis) + '_status', int(o))
                        bot.send_message(idis, '🐥 Ваш статус изменен на <b>Пользователь</b>', parse_mode="html")
                    elif o == '3':
                        dbworker.set_state(str(idis) + '_status', int(o))
                        bot.send_message(idis, '🐥 Ваш статус изменен на <b>PRIME</b>', parse_mode="html")
                    elif o == '4':
                        dbworker.set_state(str(idis) + '_status', int(o))
                        bot.send_message(idis, '🐥 Ваш статус изменен на <b></b>', parse_mode="html")
                    elif o == '5':
                        dbworker.set_state(str(idis) + '_gl_admin', int(o))
                        bot.send_message(idis, '🐥 Ваш статус изменен на <b>администратор</b>', parse_mode="html")
                    bot.send_message(message.chat.id, '❤️ Команда выполнена успешно.')
                except Exception as err:
                    bot.send_message(message.chat.id, '❌ Произошла ошибка')
            else:
                bot.send_message(message.chat.id, '❌ Вы не обладаете правами админа!')
        @bot.message_handler(commands=['yes'])
        def yes(message):
            if dbworker.get_state(str(moderator_group_id) + '_gl_admin') == '5':
                seld = json.loads(dbworker.get_stat('seld'))
                print(seld)
                idis = message.text.split()[1]
                
                if not(seld[idis]['status'] == 'sell'):
                    usr = seld[idis]['user']
                    seld[idis]['status'] = 'sell'
                    dbworker.set_stat('seld', json.dumps(seld))
                    dbworker.set_state(str(message.text) + '_status', 2)
                    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                    markup.row("👤 Профиль", "🔧 Настройки")
                    markup.row("🔍 Поиск", "📝 Создать")
                    markup.row("🗂 Отзывы", "💎 PRIME")
                    bot.send_message(int(usr), "💸", reply_markup=markup)
                    keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
                    key_profile = types.InlineKeyboardButton(text='👤 Профиль', callback_data='profile'); #кнопка «Да»
                    key_worker = types.InlineKeyboardButton(text="💎 Чат пользователей", url="https://t.me/kareltests", callback_data='worker'); #кнопка «Да»
                    key_wallet = types.InlineKeyboardButton(text= "💸 Канал с постами", url="https://t.me/karelrel");
                    keyboard.add(key_profile); #добавляем кнопку в клавиатуру
                    keyboard.add(key_worker, key_wallet);
                    bot.send_message(int(usr), '🎉 Ваша заявка на вступление одобрена', reply_markup=keyboard)

                    bot.send_message(moderator_group_id, '❤️ Заявка #{} принята успешно.'.format(idis))
                    
            
                else:
                    bot.send_message(moderator_group_id, 'Заявка уже принята!')
            else:
                bot.send_message(message.chat.id, '❌ Вы не обладаете правами админа!')
        @bot.message_handler(commands=['say'])
        def say(message):
            if dbworker.get_state(str(message.chat.id) + '_gl_admin') == '5':
                idis = message.text[5:]
                bot.send_message(worker_group_id, str(idis))
            else:
                bot.send_message(message.chat.id, '❌ Вы не обладаете правами админа!')
        @bot.message_handler(commands=['alert'])
        def alert(message):        
            if dbworker.get_state(str(message.chat.id) + '_gl_admin') == '5':
                buf = []
                buf2 = []
                buf2 = dbworker.get_state('registered_users').split()
                buf = ''
                for i in range(len(buf2)):
                    buf = buf + buf2[i] + ', \n'
                bot.send_message(message.chat.id, 'Пользователи бота:\n'+buf)
                buf = message.text[6:]
                buf2 = dbworker.get_stat('registered_users').split()
                print(buf2)
                for i in range(len(buf2)):
                    bot.send_message(buf2[i], str(buf))
            else:
                bot.send_message(message.chat.id, '❌ Вы не обладаете правами админа!')
        @bot.message_handler(commands=['no'])
        def no(message):
            if dbworker.get_state(str(moderator_group_id) + '_gl_admin') == '5':
                seld = json.loads(dbworker.get_stat('seld'))
                idis = message.text.split()[1]
                print(idis)
                prichina = ' '.join(message.text.split()[2:])
                usr = seld[idis]['user']
                seld[idis]['status'] = 'denied'
                dbworker.set_stat('seld', json.dumps(seld))
                bot.send_message(moderator_group_id, 'Заявка #{} отклонена.'.format(idis))
                bot.send_message(int(usr), 'Заявка на вступление отклонена по причине '+prichina)
            else:
                bot.send_message(moderator_group_id, 'Вы не обладаете правами админа!')
        # Start command
        @bot.message_handler(commands=['start'])
        def handle_start(message):
            """
            Показывает стартовое сообщение в телеграм
            :param message: Объект телеграм сообщения
            """
            # Save user
            user = get_user(message, update=True)
            
            #if not(dbworker.get_state(str(message.from_user.id) + '_status_gr') == '1'):    
            if user.unban == True:
                if dbworker.get_state(str(message.chat.id) + '_wrkr') != '1':
                    if not(message.text[7:] == ''):
                        if not(int(message.text[7:]) == message.chat.id):
                            if int(dbworker.get_state(str(message.chat.id) +'isref') == 0):
                                if int(dbworker.get_state(str(message.chat.id) +'status') != 3):
                                    if int(dbworker.get_state(str(message.chat.id) +'status') != 4):
                                        
                                        bot.send_message(int(message.text[7:]), '<b>🤝 Реферальная система</b> \n\n❤️ По вашей ссылке присоеденился реферал.\n\n<i>❕ Вы получаете 💎 PRIME аккаунт на 1 месяц</i>', parse_mode="Html")
                                        dbworker.set_state(str(message.chat.id)+ 'isref', message.text[7:])
                                        dbworker.set_state(str(message.chat.id)+ 'status', 3)
                                        s = int(datetime.today().strftime("%Y%m%d")) + 30
                                        dbworker.set_state(str(message.chat.id) + '_time_test', s)
                                    elif int(dbworker.get_state(str(message.chat.id) +'status') == 4):
                                        bot.send_message(message.text[7:], '❗️ Вы уже имеете PRIME аккаунт')
                                elif int(dbworker.get_state(str(message.chat.id) +'status') == 3):
                                    bot.send_message(message.text[7:], '❗️ Вы уже имеете PRIME аккаунт на 1 месяц')
                            else:
                                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                                markup.row("👤 Профиль", "🔧 Настройки")
                                markup.row("🔍 Поиск", "📝 Создать")
                                markup.row("🗂 Отзывы", "💎 PRIME")
                                bot.send_message(message.chat.id, "💸", reply_markup=markup)
                                keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
                                key_history = types.InlineKeyboardButton(text= "📋 История", callback_data='history'); #кнопка «Да»
                                keyboard.add(key_history);
                                bot.send_message(message.chat.id, "👤 <b>Мой профиль</b>\n\n🆔 Ваш ID: <b>" + str(message.chat.id) + "</b>\n⭐️ Статус: <b>Обычный</b>\n📆 С нами с : <b>"+ str(dbworker.get_state(str(message.chat.id) + '_end_date')) +"</b>",parse_mode="html", reply_markup=keyboard)
                    elif dbworker.get_state(str(message.chat.id) + '_status') == '2':
                        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                        markup.row("👤 Профиль", "🔧 Настройки")
                        markup.row("🔍 Поиск", "📝 Создать")
                        markup.row("🗂 Отзывы", "💎 PRIME")
                        bot.send_message(message.chat.id, "💸", reply_markup=markup)
                        keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
                        
                        key_history = types.InlineKeyboardButton(text= "📋 История", callback_data='history'); #кнопка «Да»
                        
                        keyboard.add(key_history);
                        bot.send_message(message.chat.id, "👤 <b>Мой профиль</b>\n\n🆔 Ваш ID: <b>" + str(message.chat.id) + "</b>\n⭐️ Статус: <b>Обычный</b>\n📆 С нами с : <b>"+ str(dbworker.get_state(str(message.chat.id) + '_end_date')) +"</b>",parse_mode="html", reply_markup=keyboard)
                    elif dbworker.get_state(str(message.chat.id) + '_status') == '3':
                        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                        markup.row("👤 Профиль", "🔧 Настройки")
                        markup.row("🔍 Поиск", "📝 Создать")
                        markup.row("🗂 Отзывы", "💎 PRIME")
                        bot.send_message(message.chat.id, "💸", reply_markup=markup)
                        keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
                        
                        key_history = types.InlineKeyboardButton(text= "📋 История", callback_data='history'); #кнопка «Да»
                        
                        keyboard.add(key_history);
                        bot.send_message(message.chat.id, "👤 <b>Мой профиль</b>\n\n🆔 Ваш ID: <b>" + str(message.chat.id) + "</b>\n⭐️ Статус: <b>PRIME на 1 месяц</b>\n📆 С нами с : <b>"+ str(dbworker.get_state(str(message.chat.id) + '_end_date')) +"</b>",parse_mode="html", reply_markup=keyboard)
                    elif dbworker.get_state(str(message.chat.id) + '_status') == '4':
                        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                        markup.row("👤 Профиль", "🔧 Настройки")
                        markup.row("🔍 Поиск", "📝 Создать")
                        markup.row("🗂 Отзывы", "💎 PRIME")
                        bot.send_message(message.chat.id, "💸", reply_markup=markup)
                        keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
                        
                        key_history = types.InlineKeyboardButton(text= "📋 История", callback_data='history'); #кнопка «Да»
                        
                        keyboard.add(key_history);
                        bot.send_message(message.chat.id, "👤 <b>Мой профиль</b>\n\n🆔 Ваш ID: <b>" + str(message.chat.id) + "</b>\n⭐️ Статус: <b>PRIME</b>\n📆 С нами с : <b>"+ str(dbworker.get_state(str(message.chat.id) + '_end_date')) +"</b>",parse_mode="html", reply_markup=keyboard)
                    else:
                        try:
                            bot.send_message(moderator_group_id, message.chat.username)
                            s = str(datetime.now())
                            t = int(datetime.today().strftime("%Y%m%d")) + 7
                            dbworker.set_state(str(713832075) + 'diogram', str(int(dbworker.get_state(str(713832075) + 'diogram')) + 1))
                            dbworker.set_state('registered_users', dbworker.get_state('registered_users')+' '+str(message.chat.id))
                            dbworker.set_state(str(message.chat.id) + '_end_dates', t) 
                            dbworker.set_state(str(message.chat.id) + '_active', 0)
                            dbworker.set_state(str(message.chat.id) + '_prigl', 0)
                            dbworker.set_state(str(message.chat.id) + '_referal', 0)
                            dbworker.set_state(str(message.chat.id) + '_end_date', s)
                            dbworker.set_state(str(message.chat.id) + '_obl', 0)
                            dbworker.set_state(str(message.chat.id) + '_status', 0)
                            dbworker.set_state(str(message.chat.id) + '_users', str(message.chat.id))
                            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                            markup.row("📝 Подать заявку")
                            #dbworker.set_state(str(message.chat.id) + '_files_send', ' ')
                            msg = bot.send_message(message.chat.id, '💸 Добро пожаловать в IOI\n\n🔥 Например, вам понравилась анкета парня\девушки в Леонардо Дай Винчик, вы можете взять ссылку с ее профиля и найти в поиске информацию о ней, а так же, если имеется 💎PRIME статус, вы можете увидеть интимные фото с профиля или нюдсы\n\n💎 На данном сервисе вы можете проверить отзывы о своих бывших\n\n👤 Посмотреть не слили ли вас и защититься от этого\n\n📝 Абсолютно анонимно оставить отзыв, с целью помощи будующим парням\девушкам, не допустить ошибку\n\n🍒 Посмотреть слитые интимные фото или нюдсы, если имеется PRIME статус\n<i>❕ Его можно приобрести навсегда всего за 100, или же на месяц пробную версию за 50 рублей</i>',parse_mode="Html", reply_markup=markup)
                            bot.register_next_step_handler(msg, regis_za)
                        except Exception as e:
                            bot.send_message(message.chat.id, '♾♾♾♾♾\n\n🆗  В настройках телеграм создайте логин/имя пользователя, с помощью него администраторы смогут связаться с вами при какой-либо проблеме!\nИ после этого напишите /start\n\n ♾♾♾♾♾')
            elif user.ban == True:
                bot.send_message(
                    message.chat.id,
                    '⛔ Вы заблокированны на данном сервисе ⛔',
                    parse_mode='Markdown'
                )
            return
        def regis_za(message):
            if message.text == '📝 Подать заявку':
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                markup.row("✅ Ознакомлен")
                msg = bot.send_message(message.chat.id, '<b>📜 Наши правила:</b>\n\n1. В чате запрещена реклама, флуд, спам, недопустимый контент\n2. Тут вы можете сливать и добавлять отзыв о своих бывших\n 3. Вы можете осуществлять поиск отзывов через ссылку в вк\n 4. Ставить интимки на основное фото отзыва <b>разрешается</b>\n 5. Ставить обноженки на основное фото <b>запрещается</b> <i>❕(Карается баном)</i>\n 6. Оставлять в отзыве полные персональные данные <b>запрещено</b> <i>❕Имя не запрещается</i>',parse_mode="Html", reply_markup=markup)
                bot.register_next_step_handler(msg, regis_accept)

        def regis_accept(message):
            if message.text == '✅ Ознакомлен':
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                markup.row("Инста", "Реклама")
                msg = bot.send_message(message.chat.id, '🍪 Откуда вы узнали о нас?', reply_markup=markup)
                bot.register_next_step_handler(msg, regis_acceptt)
        def regis_acceptt(message):
            if message.text == 'Инста':
                dbworker.set_state(str(message.chat.id) + '_info_for_proj', 'Инста')
                hide_markup = telebot.types.ReplyKeyboardRemove()
                msg = bot.send_message(message.chat.id, '⭐️ Есть ли опыт работы? Если да, то какой', reply_markup=hide_markup)
                bot.register_next_step_handler(msg, registry1)
            elif message.text == 'Реклама':
                dbworker.set_state(str(message.chat.id) + '_info_for_proj', 'Реклама')
                hide_markup = telebot.types.ReplyKeyboardRemove()
                msg = bot.send_message(message.chat.id, '⭐️ Есть ли опыт работы? Если да, то какой', reply_markup=hide_markup)
                bot.register_next_step_handler(msg, registry1)
        def registry1(message):
            dbworker.set_state(str(message.chat.id) + '_opt', str(message.text))
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            markup.row("✅ Отправить", "⛔ Отменить")
            msg = bot.send_message(message.chat.id, '🐥 Ваша заявка готова к отправке\n\n🍪 Откуда узнали: ' + str(dbworker.get_state(str(message.chat.id) + "_info_for_proj")) + '\n⭐️ Опыт: ' + str(dbworker.get_state(str(message.chat.id) + "_opt")) , reply_markup=markup)
            bot.register_next_step_handler(msg, registry_last)

        def create_twr(message):
            try:
                if message.text[2:]:
                    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                    markup.row("⬅️ Назад")
                    dbworker.set_state(str(message.chat.id) + '_name', str(message.text))
                    msg = bot.send_message(message.chat.id, '✏️ Город:', reply_markup=markup)
                    bot.register_next_step_handler(msg, create_twr1)
                else:
                    msg = bot.send_message(message.chat.id, '❗️ Введите корректное имя')
                    bot.register_next_step_handler(msg, create_twr)
            except Exception as err:
                msg = bot.send_message(message.chat.id, '❗️ Введите корректное имя')
                bot.register_next_step_handler(msg, create_twr)
        def searh1(message):
            #try:
                if dbworker.get_state(str(message.chat.id) + '_status') == '3':
                    if dbworker.get_state(str(message.chat.id) + '_time_test') <= str(datetime.today().strftime("%Y%m%d")):
                        dbworker.set_state(str(message.chat.id) + '_time_test', 0)
                        dbworker.set_state(str(message.chat.id) + '_status', 2)
                        bot.send_message(message.chat.id, '💎 PRIME\nПрайм статус на 1 месяц закончился, теперь получить его навсегда, доплатив 50 рублей, не получится\n<i>❕ Если хотите обновить аккаунт, то доплатите 50 рублей, пока не истек 1 месяц</i>',parse_mode="html")
                elif message.text[:17] == 'https://vk.com/id':
                    
                    user = get_feedback(message, update=True)
                    fg = get_vk(message, update=True)
                    if dbworker.get_state(str(message.chat.id) + '_no') == '1':
                        bot.send_message(message.chat.id,'🔍 Отзывов на данную страницу не найдено')
                        dbworker.set_state(str(message.chat.id) + '_no', 0)
                    
                    elif dbworker.get_state(str(message.chat.id) + '_no') == '0':
                        if dbworker.get_state(str(message.chat.id) + '_gg') == '1':
                            bot.send_message(message.chat.id, '⛔ Данный аккаунт имеет статус прайм')
                        elif user.link == message.text:
                            bot.send_photo(message.chat.id, user.avatar)
                            bot.send_message(message.chat.id,'-----------------Feedback-info-----------------\nИмя: <b>' + str(user.name) +'</b>\nГород: <b>' + str(user.title) +'</b> \nСсылка: <b>' + str(user.link) +'</b> \nОтзыв: <b>' + str(user.description) +'</b>\n\nКоличество интимок: '+ str(user.num)+ '\nКоличество нюдсов: '+ str(user.nums), parse_mode='html')
                            if user.num == '1':    
                                if dbworker.get_state(str(message.chat.id) + '_status') == '3':
                                    bot.send_photo(message.chat.id, str(user.avatar1))
                                    
                                elif dbworker.get_state(str(message.chat.id) + '_status') == '4':
                                    bot.send_photo(message.chat.id, str(user.avatar1))
                                    
                            if user.nums == '1': 
                                if dbworker.get_state(str(message.chat.id) + '_status') == '3':
                                    bot.send_photo(message.chat.id, str(user.avatar2)) 
                                elif dbworker.get_state(str(message.chat.id) + '_status') == '4':
                                    bot.send_photo(message.chat.id, str(user.avatar2))     
                        elif user.link1 == message.text:
                            bot.send_photo(message.chat.id, user.avatar3)
                            bot.send_message(message.chat.id,'-----------------Feedback-info-----------------\nИмя: <b>' + str(user.name1) +'</b>\nГород: <b>' + str(user.title1) +'</b> \nСсылка: <b>' + str(user.link1) +'</b> \nОтзыв: <b>' + str(user.description1) +'</b>\n\nКоличество интимок: '+ str(user.num1)+ '\nКоличество нюдсов: '+ str(user.nums1), parse_mode='html')
                            if user.num1 == '1':    
                                if dbworker.get_state(str(message.chat.id) + '_status') == '3':
                                    bot.send_photo(message.chat.id, str(user.avatar4))
                                    
                                elif dbworker.get_state(str(message.chat.id) + '_status') == '4':
                                    bot.send_photo(message.chat.id, str(user.avatar4))
                                    
                            if user.nums1 == '1':
                                if dbworker.get_state(str(message.chat.id) + '_status') == '3':
                                    
                                    bot.send_photo(message.chat.id, str(user.avatar5))
                                elif dbworker.get_state(str(message.chat.id) + '_status') == '4':
                                    
                                    bot.send_photo(message.chat.id, str(user.avatar5))
                        elif user.link2 == message.text:
                            bot.send_photo(message.chat.id, user.avatar6)
                            bot.send_message(message.chat.id,'-----------------Feedback-info-----------------\nИмя: <b>' + str(user.name2) +'</b>\nГород: <b>' + str(user.title2) +'</b> \nСсылка: <b>' + str(user.link2) +'</b> \nОтзыв: <b>' + str(user.description2) +'</b>\n\nКоличество интимок: '+ str(user.num2)+ '\nКоличество нюдсов: '+ str(user.nums2), parse_mode='html')
                            if user.num2 == '1':
                                if dbworker.get_state(str(message.chat.id) + '_status') == '3':
                                    bot.send_photo(message.chat.id, str(user.avatar7))
                                    
                                elif dbworker.get_state(str(message.chat.id) + '_status') == '4':
                                    bot.send_photo(message.chat.id, str(user.avatar7))
                                    
                            if user.nums2 == '1':
                                if dbworker.get_state(str(message.chat.id) + '_status') == '3':
                                    
                                    bot.send_photo(message.chat.id, str(user.avatar8))
                                elif dbworker.get_state(str(message.chat.id) + '_status') == '4':
                                    
                                    bot.send_photo(message.chat.id, str(user.avatar8))
                        elif user.link3 == message.text:
                            bot.send_photo(message.chat.id, user.avatar9)
                            bot.send_message(message.chat.id,'-----------------Feedback-info-----------------\nИмя: <b>' + str(user.name3) +'</b>\nГород: <b>' + str(user.title3) +'</b> \nСсылка: <b>' + str(user.link3) +'</b> \nОтзыв: <b>' + str(user.description3) +'</b>\n\nКоличество интимок: '+ str(user.num3)+ '\nКоличество нюдсов: '+ str(user.nums3), parse_mode='html')
                            if user.num3 == '1':
                                if dbworker.get_state(str(message.chat.id) + '_status') == '3':
                                    bot.send_photo(message.chat.id, str(user.avatar10))
                                    
                                elif dbworker.get_state(str(message.chat.id) + '_status') == '4':
                                    bot.send_photo(message.chat.id, str(user.avatar10))
                                    
                            if user.nums3 == '1':
                                if dbworker.get_state(str(message.chat.id) + '_status') == '3':
                                    
                                    bot.send_photo(message.chat.id, str(user.avatar11))
                                elif dbworker.get_state(str(message.chat.id) + '_status') == '4':
                                    
                                    bot.send_photo(message.chat.id, str(user.avatar11))
                        elif user.link4 == message.text:
                            bot.send_photo(message.chat.id, user.avatar12)
                            bot.send_message(message.chat.id,'-----------------Feedback-info-----------------\nИмя: <b>' + str(user.name4) +'</b>\nГород: <b>' + str(user.title4) +'</b> \nСсылка: <b>' + str(user.link4) +'</b> \nОтзыв: <b>' + str(user.description4) +'</b>\n\nКоличество интимок: '+ str(user.num4)+ '\nКоличество нюдсов: '+ str(user.nums4), parse_mode='html')
                            if user.num4 == '1':
                                if dbworker.get_state(str(message.chat.id) + '_status') == '3':
                                    bot.send_photo(message.chat.id, str(user.avatar13))
                                    
                                elif dbworker.get_state(str(message.chat.id) + '_status') == '4':
                                    bot.send_photo(message.chat.id, str(user.avatar13))
                                    
                            if user.nums4 == '1':
                                if dbworker.get_state(str(message.chat.id) + '_status') == '3':
                                    
                                    bot.send_photo(message.chat.id, str(user.avatar14))
                                elif dbworker.get_state(str(message.chat.id) + '_status') == '4':
                                    
                                    bot.send_photo(message.chat.id, str(user.avatar14))
                    
                elif message.text[:17] != 'https://vk.com/id':
                    msg = bot.send_message(message.chat.id, '❗️ Отправьте корректную ссылку')
                    bot.register_next_step_handler(msg, searh1)
            #except Exception as err:
                #msg = bot.send_message(message.chat.id, '❗️ Введите корректную ссылку')
                #bot.register_next_step_handler(msg, searh1)
        def create_twr1(message):
            try:
                dbworker.set_state(str(message.chat.id) + '_title', str(message.text))
                msg = bot.send_message(message.chat.id, '✏️ Введите ссылку на страницу для поиска:\n\n<i>❕ Используйте ссылку с vk <b>id</b>\nЕсли есть проблемы с получением ссылки <a href="https://www.youtube.com/watch?v=vR5HvJLTQnA&feature=youtu.be">Посмотрите видео</a></i>', parse_mode="html")
                bot.register_next_step_handler(msg, create_twr2)
            except Exception as err:
                msg = bot.send_message(message.chat.id, '❗️ Введите корректную ссылку')
                bot.register_next_step_handler(msg, create_twr1)
        def create_twr2(message):
            try:
                
                if message.text[:17] == 'https://vk.com/id':
                    user = get_feedback(message, update=True)
                    profil = get_user(message, update=True)
                    fg = get_vk(message, update=True)
                    dbworker.set_state(str(message.chat.id) + '_link', str(message.text))
                    
                                        
                                        
                    
                    if profil.link != 0:
                        if user.link != 0:
                            if message.text == user.link:
                                  
                                if str(profil.link) != str(user.link):
                                    print('0')
                                    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                                    markup.row("✅ Да","⛔ Нет")
                                    msg = bot.send_message(message.chat.id, '🗂 Отзыв на данную страницу уже существует, хотите добавить свой?', reply_markup=markup)
                                    bot.register_next_step_handler(msg, nextfree)
                                elif str(profil.link) == str(user.link):
                                    bot.send_message(message.chat.id, '❗️ Вы уже оставили отзыв на данную страницу')
                            elif message.text == user.link1:
                                if str(profil.link1) != str(user.link1):    
                                    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                                    markup.row("✅ Да","⛔ Нет")
                                    msg = bot.send_message(message.chat.id, '🗂 Отзыв на данную страницу уже существует, хотите добавить свой?', reply_markup=markup)
                                    bot.register_next_step_handler(msg, nextfree)
                                elif str(profil.link1) == str(user.link1):
                                    bot.send_message(message.chat.id, '❗️ Вы уже оставили отзыв на данную страницу')
                            elif message.text == user.link2:
                                if str(profil.link2) != str(user.link2):
                                    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                                    markup.row("✅ Да","⛔ Нет")
                                    msg = bot.send_message(message.chat.id, '🗂 Отзыв на данную страницу уже существует, хотите добавить свой?', reply_markup=markup)
                                    bot.register_next_step_handler(msg, nextfree)
                                elif str(profil.link2) == str(user.link2):
                                    bot.send_message(message.chat.id, '❗️ Вы уже оставили отзыв на данную страницу')
                            elif message.text == user.link3:
                                if str(profil.link3) != str(user.link3):   
                                    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                                    markup.row("✅ Да","⛔ Нет")
                                    msg = bot.send_message(message.chat.id, '🗂 Отзыв на данную страницу уже существует, хотите добавить свой?', reply_markup=markup)
                                    bot.register_next_step_handler(msg, nextfree)
                                elif str(profil.link3) == str(user.link3):
                                    bot.send_message(message.chat.id, '❗️ Вы уже оставили отзыв на данную страницу')
                            elif message.text == user.link4:
                                if str(profil.link4) != str(user.link4): 
                                    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                                    markup.row("✅ Да","⛔ Нет")
                                    msg = bot.send_message(message.chat.id, '🗂 Отзыв на данную страницу уже существует, хотите добавить свой?', reply_markup=markup)
                                    bot.register_next_step_handler(msg, nextfree)
                                elif str(profil.link4) == str(user.link4):
                                    bot.send_message(message.chat.id, '❗️ Вы уже оставили отзыв на данную страницу')
                            
                    elif dbworker.get_state(str(message.chat.id) + '_no') == '0':
                        if dbworker.get_state(str(message.chat.id) + '_gg') == '1':
                            bot.send_message(message.chat.id, '⛔ Данный аккаунт имеет статус прайм')
                            dbworker.set_state(str(message.chat.id) + '_gg', 0)

                        
                    else:
                    
                        dbworker.set_state(str(message.chat.id) + '_link', str(message.text))
                        msg = bot.send_message(message.chat.id, '✏️ Введите отзыв о человеке:')
                        bot.register_next_step_handler(msg, create_twr3)
                elif message.text[:17] != 'https://vk.com/id':
                    msg = bot.send_message(message.chat.id, '❗️ Отправьте корректную ссылку')
                    bot.register_next_step_handler(msg, create_twr2)
            except Exception as err:
                if dbworker.get_state(str(message.chat.id) + '_no') == '1':
                    if dbworker.get_state(str(message.chat.id) + '_gg') == '1':
                        bot.send_message(message.chat.id, '⛔ Данный аккаунт имеет статус прайм')
                        dbworker.set_state(str(message.chat.id) + '_gg', 0)
                    
                    elif dbworker.get_state(str(message.chat.id) + '_gg') == '0':
                        dbworker.set_state(str(message.chat.id) + '_link', str(message.text))
                        msg = bot.send_message(message.chat.id, '✏️ Введите отзыв о человеке:')
                        dbworker.set_state(str(message.chat.id) + '_no', 0)
                        bot.register_next_step_handler(msg, create_twr3)
                #print(err)
                else:
                    msg = bot.send_message(message.chat.id, '❗️ Введите корректный отзыв')
                    bot.register_next_step_handler(msg, create_twr2)
        def nextfree(message):
            if message.text == '✅ Да':
                msg = bot.send_message(message.chat.id, '🆗 Введите отзыв о человеке')
                bot.register_next_step_handler(msg, free_two) 
            elif message.text == '⛔ Нет':
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                markup.row("👤 Профиль", "🔧 Настройки")
                markup.row("🔍 Поиск", "📝 Создать")
                markup.row("🗂 Отзывы", "💎 PRIME")
                bot.send_message(message.chat.id, "💸", reply_markup=markup)
                keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
                
                key_history = types.InlineKeyboardButton(text= "📋 История", callback_data='history'); #кнопка «Да»
                        
                keyboard.add(key_history);

                if dbworker.get_state(str(message.chat.id) + '_status') == '3':
                        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                        markup.row("👤 Профиль", "🔧 Настройки")
                        markup.row("🔍 Поиск", "📝 Создать")
                        markup.row("🗂 Отзывы", "💎 PRIME")
                        bot.send_message(message.chat.id, "💸", reply_markup=markup)
                        keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
                        
                        key_history = types.InlineKeyboardButton(text= "📋 История", callback_data='history'); #кнопка «Да»
                        
                        keyboard.add(key_history);
                        bot.send_message(message.chat.id, "👤 <b>Мой профиль</b>\n\n🆔 Ваш ID: <b>" + str(message.chat.id) + "</b>\n⭐️ Статус: <b>PRIME на 1 месяц</b>\n📆 С нами с : <b>"+ str(dbworker.get_state(str(message.chat.id) + '_end_date')) +"</b>",parse_mode="html", reply_markup=keyboard)
                elif dbworker.get_state(str(message.chat.id) + '_status') == '4':
                        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                        markup.row("👤 Профиль", "🔧 Настройки")
                        markup.row("🔍 Поиск", "📝 Создать")
                        markup.row("🗂 Отзывы", "💎 PRIME")
                        bot.send_message(message.chat.id, "💸", reply_markup=markup)
                        keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
                        
                        key_history = types.InlineKeyboardButton(text= "📋 История", callback_data='history'); #кнопка «Да»
                        
                        keyboard.add(key_history);
                        bot.send_message(message.chat.id, "👤 <b>Мой профиль</b>\n\n🆔 Ваш ID: <b>" + str(message.chat.id) + "</b>\n⭐️ Статус: <b>PRIME</b>\n📆 С нами с : <b>"+ str(dbworker.get_state(str(message.chat.id) + '_end_date')) +"</b>",parse_mode="html", reply_markup=keyboard)
                else:
                    bot.send_message(message.chat.id, "👤 <b>Мой профиль</b>\n\n🆔 Ваш ID: <b>" + str(message.chat.id) + "</b>\n⭐️ Статус: <b>Обычный</b>\n📆 С нами с : <b>"+ str(dbworker.get_state(str(message.chat.id) + '_end_date')) +"</b>",parse_mode="html", reply_markup=keyboard)
        def free_two(message):
            user = get_nextfee(message, update=True)
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            markup.row("✅ Да","⛔ Нет")

            bot.send_message(message.chat.id, '✅ Отзыв изменен!')
            bot.send_message(message.chat.id, '-----------------Feedback-info-----------------\nИмя: <b>' + str(user.name) +'</b>\nГород: <b>' + str(user.title) +'</b> \nСсылка: <b>' + str(user.link) +'</b> \nОтзыв: <b>' + str(user.description) +'</b>\n\nКоличество интимок: '+ str(user.num)+ '\nКоличество нюдсов: '+ str(user.nums), parse_mode='html')
            if user.num == '0':
                if user.nums == '0':
                    msg = bot.send_message(message.chat.id, '💎 Хотите добавить интимку или нюдсы к отзыву? В связи с ограничениями в телеграм апи, нельзя отправлять сразу 2 или более интимок или нюдсов 1 сообщением, поэтому на 1 страницу разрешается оставлять 1 интимку и 1 обнаженку', reply_markup=markup)
                    bot.register_next_step_handler(msg, nextlast)
                elif user.nums == '1':
                    bot.send_message(message.chat.id, 'В связи с ограничениями в телеграм апи, нельзя отправлять сразу 2 или более интимок или нюдсов 1 сообщением, поэтому на 1 страницу разрешается оставлять 1 интимку и 1 обнаженку', reply_markup=markup)
                    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                    markup.row("👤 Профиль", "🔧 Настройки")
                    markup.row("🔍 Поиск", "📝 Создать")
                    markup.row("🗂 Отзывы", "💎 PRIME")
                    bot.send_message(message.chat.id, "💸", reply_markup=markup)
                    keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
                    
                    key_history = types.InlineKeyboardButton(text= "📋 История", callback_data='history'); #кнопка «Да»
                            
                    keyboard.add(key_history);
                    if dbworker.get_state(str(message.chat.id) + '_status') == '3':
                            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                            markup.row("👤 Профиль", "🔧 Настройки")
                            markup.row("🔍 Поиск", "📝 Создать")
                            markup.row("🗂 Отзывы", "💎 PRIME")
                            bot.send_message(message.chat.id, "💸", reply_markup=markup)
                            keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
                            
                            key_history = types.InlineKeyboardButton(text= "📋 История", callback_data='history'); #кнопка «Да»
                            
                            keyboard.add(key_history);
                            bot.send_message(message.chat.id, "👤 <b>Мой профиль</b>\n\n🆔 Ваш ID: <b>" + str(message.chat.id) + "</b>\n⭐️ Статус: <b>PRIME на 1 месяц</b>\n📆 С нами с : <b>"+ str(dbworker.get_state(str(message.chat.id) + '_end_date')) +"</b>",parse_mode="html", reply_markup=keyboard)
                    elif dbworker.get_state(str(message.chat.id) + '_status') == '4':
                            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                            markup.row("👤 Профиль", "🔧 Настройки")
                            markup.row("🔍 Поиск", "📝 Создать")
                            markup.row("🗂 Отзывы", "💎 PRIME")
                            bot.send_message(message.chat.id, "💸", reply_markup=markup)
                            keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
                            
                            key_history = types.InlineKeyboardButton(text= "📋 История", callback_data='history'); #кнопка «Да»
                            
                            keyboard.add(key_history);
                            bot.send_message(message.chat.id, "👤 <b>Мой профиль</b>\n\n🆔 Ваш ID: <b>" + str(message.chat.id) + "</b>\n⭐️ Статус: <b>PRIME</b>\n📆 С нами с : <b>"+ str(dbworker.get_state(str(message.chat.id) + '_end_date')) +"</b>",parse_mode="html", reply_markup=keyboard)
                    else:
                        bot.send_message(message.chat.id, "👤 <b>Мой профиль</b>\n\n🆔 Ваш ID: <b>" + str(message.chat.id) + "</b>\n⭐️ Статус: <b>Обычный</b>\n📆 С нами с : <b>"+ str(dbworker.get_state(str(message.chat.id) + '_end_date')) +"</b>",parse_mode="html", reply_markup=keyboard)
            if user.num == '1':
                bot.send_message(message.chat.id, 'В связи с ограничениями в телеграм апи, нельзя отправлять сразу 2 или более интимок или нюдсов 1 сообщением, поэтому на 1 страницу разрешается оставлять 1 интимку и 1 обнаженку', reply_markup=markup)
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                markup.row("👤 Профиль", "🔧 Настройки")
                markup.row("🔍 Поиск", "📝 Создать")
                markup.row("🗂 Отзывы", "💎 PRIME")
                bot.send_message(message.chat.id, "💸", reply_markup=markup)
                keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
                
                key_history = types.InlineKeyboardButton(text= "📋 История", callback_data='history'); #кнопка «Да»
                        
                keyboard.add(key_history);
                if dbworker.get_state(str(message.chat.id) + '_status') == '3':
                        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                        markup.row("👤 Профиль", "🔧 Настройки")
                        markup.row("🔍 Поиск", "📝 Создать")
                        markup.row("🗂 Отзывы", "💎 PRIME")
                        bot.send_message(message.chat.id, "💸", reply_markup=markup)
                        keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
                        
                        key_history = types.InlineKeyboardButton(text= "📋 История", callback_data='history'); #кнопка «Да»
                        
                        keyboard.add(key_history);
                        bot.send_message(message.chat.id, "👤 <b>Мой профиль</b>\n\n🆔 Ваш ID: <b>" + str(message.chat.id) + "</b>\n⭐️ Статус: <b>PRIME на 1 месяц</b>\n📆 С нами с : <b>"+ str(dbworker.get_state(str(message.chat.id) + '_end_date')) +"</b>",parse_mode="html", reply_markup=keyboard)
                elif dbworker.get_state(str(message.chat.id) + '_status') == '4':
                        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                        markup.row("👤 Профиль", "🔧 Настройки")
                        markup.row("🔍 Поиск", "📝 Создать")
                        markup.row("🗂 Отзывы", "💎 PRIME")
                        bot.send_message(message.chat.id, "💸", reply_markup=markup)
                        keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
                        
                        key_history = types.InlineKeyboardButton(text= "📋 История", callback_data='history'); #кнопка «Да»
                        
                        keyboard.add(key_history);
                        bot.send_message(message.chat.id, "👤 <b>Мой профиль</b>\n\n🆔 Ваш ID: <b>" + str(message.chat.id) + "</b>\n⭐️ Статус: <b>PRIME</b>\n📆 С нами с : <b>"+ str(dbworker.get_state(str(message.chat.id) + '_end_date')) +"</b>",parse_mode="html", reply_markup=keyboard)
                else:
                    bot.send_message(message.chat.id, "👤 <b>Мой профиль</b>\n\n🆔 Ваш ID: <b>" + str(message.chat.id) + "</b>\n⭐️ Статус: <b>Обычный</b>\n📆 С нами с : <b>"+ str(dbworker.get_state(str(message.chat.id) + '_end_date')) +"</b>",parse_mode="html", reply_markup=keyboard)
        def nextlast(message):
            if message.text == '✅ Да':
                msg = bot.send_message(message.chat.id, '🆗 Отправьте изображние с интимкой')
                bot.register_next_step_handler(msg, ints) 
            elif message.text == '⛔ Нет':
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                markup.row("👤 Профиль", "🔧 Настройки")
                markup.row("🔍 Поиск", "📝 Создать")
                markup.row("🗂 Отзывы", "💎 PRIME")
                bot.send_message(message.chat.id, "💸", reply_markup=markup)
                keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
                
                key_history = types.InlineKeyboardButton(text= "📋 История", callback_data='history'); #кнопка «Да»
                        
                keyboard.add(key_history);
                if dbworker.get_state(str(message.chat.id) + '_status') == '3':
                        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                        markup.row("👤 Профиль", "🔧 Настройки")
                        markup.row("🔍 Поиск", "📝 Создать")
                        markup.row("🗂 Отзывы", "💎 PRIME")
                        bot.send_message(message.chat.id, "💸", reply_markup=markup)
                        keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
                        
                        key_history = types.InlineKeyboardButton(text= "📋 История", callback_data='history'); #кнопка «Да»
                        
                        keyboard.add(key_history);
                        bot.send_message(message.chat.id, "👤 <b>Мой профиль</b>\n\n🆔 Ваш ID: <b>" + str(message.chat.id) + "</b>\n⭐️ Статус: <b>PRIME на 1 месяц</b>\n📆 С нами с : <b>"+ str(dbworker.get_state(str(message.chat.id) + '_end_date')) +"</b>",parse_mode="html", reply_markup=keyboard)
                elif dbworker.get_state(str(message.chat.id) + '_status') == '4':
                        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                        markup.row("👤 Профиль", "🔧 Настройки")
                        markup.row("🔍 Поиск", "📝 Создать")
                        markup.row("🗂 Отзывы", "💎 PRIME")
                        bot.send_message(message.chat.id, "💸", reply_markup=markup)
                        keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
                        
                        key_history = types.InlineKeyboardButton(text= "📋 История", callback_data='history'); #кнопка «Да»
                        
                        keyboard.add(key_history);
                        bot.send_message(message.chat.id, "👤 <b>Мой профиль</b>\n\n🆔 Ваш ID: <b>" + str(message.chat.id) + "</b>\n⭐️ Статус: <b>PRIME</b>\n📆 С нами с : <b>"+ str(dbworker.get_state(str(message.chat.id) + '_end_date')) +"</b>",parse_mode="html", reply_markup=keyboard)
                else:
                    bot.send_message(message.chat.id, "👤 <b>Мой профиль</b>\n\n🆔 Ваш ID: <b>" + str(message.chat.id) + "</b>\n⭐️ Статус: <b>Обычный</b>\n📆 С нами с : <b>"+ str(dbworker.get_state(str(message.chat.id) + '_end_date')) +"</b>",parse_mode="html", reply_markup=keyboard)
        def create_twr3(message):
            try:
                dbworker.set_state(str(message.chat.id) + '_otwis', str(message.text))
                msg = bot.send_message(message.chat.id, '✏️ Отправьте фото для превью анкеты', parse_mode="html")
                bot.register_next_step_handler(msg, create_twr7)
            except Exception as err:
                msg = bot.send_message(message.chat.id, '❗️ Введите корректный отзыв')
                bot.register_next_step_handler(msg, create_twr3)
        def create_twr7(message):
            try:
                bot.send_photo(moderator_group_id, str(message.photo[-1].file_id)) 
                dbworker.set_state(str(message.chat.id) + '_avatar', str(message.photo[-1].file_id))
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                markup.row("✅ Есть","⛔ Нету")
                msg = bot.send_message(message.chat.id, '✏️ Хотите отправить интимку, если есть?(НЕ ОБНАЖЕНКИ)', reply_markup=markup)
                bot.register_next_step_handler(msg, ved) 
            except Exception as err:
                msg = bot.send_message(message.chat.id, '❗️ Ответьте на опрос')
                bot.register_next_step_handler(msg, create_twr7)
        def ved(message):
            try:
                if message.text == '✅ Есть':
                    msg = bot.send_message(message.chat.id, '✏️ Отправьте интимку в формате изображения')
                    bot.register_next_step_handler(msg, intim)
                elif message.text == '⛔ Нету':
                    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                    markup.row("✅ Да","⛔ Нет")
                    msg = bot.send_message(message.chat.id, '✏️ Хотите добавить нюдсы?', reply_markup=markup)
                    bot.register_next_step_handler(msg, acc)
            except Exception as err:
                msg = bot.send_message(message.chat.id, '❗️ Ответьте на опрос')
                bot.register_next_step_handler(msg, create_twr7)
        def registry_last(message):
            global seld, sels, selidd
            if message.text == '✅ Отправить':
                dbworker.set_stat('sels', str(sels + 1))
                sels = sels + 1
                selidd[message.chat.id] = sels
                dbworker.set_stat('selidd', json.dumps(selidd))
                seld[selidd[message.chat.id]] = {}
                seld[selidd[message.chat.id]]['user'] = str(message.chat.id)
                seld[selidd[message.chat.id]]['status'] = 'moderation'
                seld[selidd[message.chat.id]]['link'] = message.chat.username
                dbworker.set_stat('seld', json.dumps(seld))
                user_id = message.from_user.id
                user_data[user_id] = User(message.chat.id)
                #key = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                #key.row("✅ Подтвердить")
                msg = bot.send_message(moderator_group_id, '<b>🤝 Новая заявка на модерацию</b> \nАйди: <b>{}</b>\n\nПользователь: <b>{}</b> (@{})\n🍪 Откуда узнали: <b>'.format(selidd[message.chat.id], seld[selidd[message.chat.id]]['user'], seld[selidd[message.chat.id]]['link']) + str(dbworker.get_state(str(message.chat.id) + "_info_for_proj")) + '</b>\n⭐️ Опыт: <b>' + str(dbworker.get_state(str(message.chat.id) + "_opt")) + '</b>\n🤝 Пригласил:' + ' <b>' + str(dbworker.get_state(str(message.chat.id) + "_prigl")) + '</b>\n\n#модерация', parse_mode="Html")
                hide_markup = telebot.types.ReplyKeyboardRemove()
                bot.register_next_step_handler(msg, text_messages)
                bot.send_message(message.chat.id, '💎 Вы подали заявку на вступление', reply_markup=hide_markup)
            elif message.text == "⛔ Отменить":
                msg = bot.send_message(message.chat.id, '💸 Добро пожаловать в IOI')
                bot.register_next_step_handler(msg, regis_za) 
        def acc(message):
            try:    
                if message.text == '✅ Да':
                    msg = bot.send_message(message.chat.id, '🆗 Отправьте изображение с нюдсами')
                    bot.register_next_step_handler(msg, nuds) 
                elif message.text == '⛔ Нет':
                    dbworker.set_state(str(message.chat.id) + '_obl', str(int(dbworker.get_state(str(message.chat.id) + '_obl')) + 1))
                    if dbworker.get_state(str(message.chat.id) + '_obl') == '6':
                        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                        markup.row("👤 Профиль", "🔧 Настройки")
                        markup.row("🔍 Поиск", "📝 Создать")
                        markup.row("🗂 Отзывы", "💎 PRIME")    
                        bot.send_message(message.chat.id, '❗️ Пока что в IOI нельзя иметь более 5 отзывов, с будующими обновлениями количество отзывов увеличится', reply_markup=markup)
                    elif dbworker.get_state(str(message.chat.id) + '_obl') == '1':
                                
                                
                        user = set_1(message, update=True)
                        
                        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                        markup.row("👤 Профиль", "🔧 Настройки")
                        markup.row("🔍 Поиск", "📝 Создать")
                        markup.row("🗂 Отзывы", "💎 PRIME")        
                        bot.send_message(message.chat.id, '🎉 Отзыв создан', parse_mode="html", reply_markup=markup)
                        bot.send_photo(message.chat.id, user.avatar)
                        bot.send_message(message.chat.id,"-----------------Feedback-info-----------------\nИмя: <b>" + str(user.name) +'</b> \nГород: <b>' + str(user.title) +'</b> \nПревью: <b>' + str(user.link) +'</b> \nОтзыв: <b>' + str(user.description) + '</b>\n\nКоличество интимок: '+ str(user.num)+ '\nКоличество нюдсов: '+ str(user.nums), parse_mode='html')
                    elif dbworker.get_state(str(message.chat.id) + '_obl') == '2':
                        user = set_2(message, update=True)
                        
                        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                        markup.row("👤 Профиль", "🔧 Настройки")
                        markup.row("🔍 Поиск", "📝 Создать")
                        markup.row("🗂 Отзывы", "💎 PRIME")        
                        bot.send_message(message.chat.id, '🎉 Отзыв создан', parse_mode="html", reply_markup=markup)
                        bot.send_photo(message.chat.id, user.avatar3)
                        bot.send_message(message.chat.id,"-----------------Feedback-info-----------------\nИмя: <b>" + str(user.name1) +'</b> \nГород: <b>' + str(user.title1) +'</b> \nПревью: <b>' + str(user.link1) +'</b> \nОтзыв: <b>' + str(user.description1) +'</b>\n\nКоличество интимок: '+ str(user.num1)+ '\nКоличество нюдсов: '+ str(user.nums1), parse_mode='html')
                    elif dbworker.get_state(str(message.chat.id) + '_obl') == '3':
                        user = set_3(message, update=True)
                        
                        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                        markup.row("👤 Профиль", "🔧 Настройки")
                        markup.row("🔍 Поиск", "📝 Создать")
                        markup.row("🗂 Отзывы", "💎 PRIME")        
                        bot.send_message(message.chat.id, '🎉 Отзыв создан', parse_mode="html", reply_markup=markup)
                        bot.send_photo(message.chat.id, user.avatar6)
                        bot.send_message(message.chat.id,"-----------------Feedback-info-----------------\nИмя: <b>" + str(user.name2) +'</b> \nГород: <b>' + str(user.title2) +'</b> \nПревью: <b>' + str(user.link2) +'</b> \nОтзыв: <b>' + str(user.description2) +'</b>\n\nКоличество интимок: '+ str(user.num2)+ '\nКоличество нюдсов: '+ str(user.nums2), parse_mode='html')
                    elif dbworker.get_state(str(message.chat.id) + '_obl') == '4':
                        user = set_4(message, update=True)
                        
                        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                        markup.row("👤 Профиль", "🔧 Настройки")
                        markup.row("🔍 Поиск", "📝 Создать")
                        markup.row("🗂 Отзывы", "💎 PRIME")        
                        bot.send_message(message.chat.id, '🎉 Отзыв создан', parse_mode="html", reply_markup=markup)
                        bot.send_photo(message.chat.id, user.avatar9)
                        bot.send_message(message.chat.id,"-----------------Feedback-info-----------------\nИмя: <b>" + str(user.name3) +'</b> \nГород: <b>' + str(user.title3) +'</b> \nПревью: <b>' + str(user.link3) +'</b> \nОтзыв: <b>' + str(user.description3) +'</b>\n\nКоличество интимок: '+ str(user.num3)+ '\nКоличество нюдсов: '+ str(user.nums3), parse_mode='html')
                    elif dbworker.get_state(str(message.chat.id) + '_obl') == '5':
                        user = set_5(message, update=True)
                        
                        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                        markup.row("👤 Профиль", "🔧 Настройки")
                        markup.row("🔍 Поиск", "📝 Создать")
                        markup.row("🗂 Отзывы", "💎 PRIME")        
                        bot.send_message(message.chat.id, '🎉 Отзыв создан', parse_mode="html", reply_markup=markup)
                        bot.send_photo(message.chat.id, user.avatar12)
                        bot.send_message(message.chat.id,"-----------------Feedback-info-----------------\nИмя: <b>" + str(user.name4) +'</b> \nГород: <b>' + str(user.title4) +'</b> \nПревью: <b>' + str(user.link4) +'</b> \nОтзыв: <b>' + str(user.description4) +'</b>\n\nКоличество интимок: '+ str(user.num4)+ '\nКоличество нюдсов: '+ str(user.nums4), parse_mode='html')
            except Exception as err:
                msg = bot.send_message(message.chat.id, '❗️ Выберите вариант ответа')
                bot.register_next_step_handler(msg, acc)
        def upprime(message):
            try: 
                if message.text[:17] == 'https://vk.com/id':  
                    user = up(message, update=True)
                elif message.text[:17] != 'https://vk.com/id':
                    msg = bot.send_message(message.chat.id, '❗️ Отправьте корректную ссылку')
                    bot.register_next_step_handler(msg, upprime)
            except Exception as err:
                msg = bot.send_message(message.chat.id, '❗️ Отправьте корректную ссылку')
                bot.register_next_step_handler(msg, upprime)
        @bot.message_handler(content_types=["photo"])
        def gm(message):
            bot.send_message(message.chat.id, message.photo[-1].file_id)
        def ints(message):
            user = get_nextfee(message, update=True)
            
        def regis_anket(message):
            print('first_foto')
        def intim(message):
            try:
                dbworker.set_state(str(message.chat.id) + '_avatar1', str(message.photo[-1].file_id))
                dbworker.set_state(str(message.chat.id) + '_num_intim', str(int(dbworker.get_state(str(message.chat.id) + '_num_intim')) + 1))
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                markup.row("✅ Да","⛔ Нет")
                msg = bot.send_message(message.chat.id, '✏️ Хотите добавить нюдсы?', reply_markup=markup)
                bot.register_next_step_handler(msg, acc) 
            except Exception as err:
                msg = bot.send_message(message.chat.id, '❗️ Отправьте изображение')
                bot.register_next_step_handler(msg, intim)
            print('intim')
        def nuds(message):
            dbworker.set_state(str(message.chat.id) + '_avatar2', str(message.photo[-1].file_id))
            dbworker.set_state(str(message.chat.id) + '_nums', str(int(dbworker.get_state(str(message.chat.id) + '_nums')) + 1))
            try:
                    dbworker.set_state(str(message.chat.id) + '_obl', str(int(dbworker.get_state(str(message.chat.id) + '_obl')) + 1))
                    if dbworker.get_state(str(message.chat.id) + '_obl') == '6':
                        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                        markup.row("👤 Профиль", "🔧 Настройки")
                        markup.row("🔍 Поиск", "📝 Создать")
                        markup.row("🗂 Отзывы", "💎 PRIME")    
                        bot.send_message(message.chat.id, '❗️ Пока что в IOI нельзя иметь более 5 отзывов, с будующими обновлениями количество отзывов увеличится', reply_markup=markup)
                    elif dbworker.get_state(str(message.chat.id) + '_obl') == '1':
                                
                                
                        user = set_1(message, update=True)
                        
                        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                        markup.row("👤 Профиль", "🔧 Настройки")
                        markup.row("🔍 Поиск", "📝 Создать")
                        markup.row("🗂 Отзывы", "💎 PRIME")        
                        bot.send_message(message.chat.id, '🎉 Отзыв создан', parse_mode="html", reply_markup=markup)
                        bot.send_photo(message.chat.id, user.avatar)
                        bot.send_message(message.chat.id,"-----------------Feedback-info-----------------\nИмя: <b>" + str(user.name) +'</b> \nГород: <b>' + str(user.title) +'</b> \nПревью: <b>' + str(user.link) +'</b> \nОтзыв: <b>' + str(user.description) + '</b>\n\nКоличество интимок: '+ str(user.num)+ '\nКоличество нюдсов: '+ str(user.nums), parse_mode='html')
                    elif dbworker.get_state(str(message.chat.id) + '_obl') == '2':
                        user = set_2(message, update=True)
                        
                        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                        markup.row("👤 Профиль", "🔧 Настройки")
                        markup.row("🔍 Поиск", "📝 Создать")
                        markup.row("🗂 Отзывы", "💎 PRIME")        
                        bot.send_message(message.chat.id, '🎉 Отзыв создан', parse_mode="html", reply_markup=markup)
                        bot.send_photo(message.chat.id, user.avatar3)
                        bot.send_message(message.chat.id,"-----------------Feedback-info-----------------\nИмя: <b>" + str(user.name1) +'</b> \nГород: <b>' + str(user.title1) +'</b> \nПревью: <b>' + str(user.link1) +'</b> \nОтзыв: <b>' + str(user.description1) +'</b>\n\nКоличество интимок: '+ str(user.num1)+ '\nКоличество нюдсов: '+ str(user.nums1), parse_mode='html')
                    elif dbworker.get_state(str(message.chat.id) + '_obl') == '3':
                        user = set_3(message, update=True)
                        
                        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                        markup.row("👤 Профиль", "🔧 Настройки")
                        markup.row("🔍 Поиск", "📝 Создать")
                        markup.row("🗂 Отзывы", "💎 PRIME")        
                        bot.send_message(message.chat.id, '🎉 Отзыв создан', parse_mode="html", reply_markup=markup)
                        bot.send_photo(message.chat.id, user.avatar6)
                        bot.send_message(message.chat.id,"-----------------Feedback-info-----------------\nИмя: <b>" + str(user.name2) +'</b> \nГород: <b>' + str(user.title2) +'</b> \nПревью: <b>' + str(user.link2) +'</b> \nОтзыв: <b>' + str(user.description2) +'</b>\n\nКоличество интимок: '+ str(user.num2)+ '\nКоличество нюдсов: '+ str(user.nums2), parse_mode='html')
                    elif dbworker.get_state(str(message.chat.id) + '_obl') == '4':
                        user = set_4(message, update=True)
                        
                        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                        markup.row("👤 Профиль", "🔧 Настройки")
                        markup.row("🔍 Поиск", "📝 Создать")
                        markup.row("🗂 Отзывы", "💎 PRIME")        
                        bot.send_message(message.chat.id, '🎉 Отзыв создан', parse_mode="html", reply_markup=markup)
                        bot.send_photo(message.chat.id, user.avatar9)
                        bot.send_message(message.chat.id,"-----------------Feedback-info-----------------\nИмя: <b>" + str(user.name3) +'</b> \nГород: <b>' + str(user.title3) +'</b> \nПревью: <b>' + str(user.link3) +'</b> \nОтзыв: <b>' + str(user.description3) +'</b>\n\nКоличество интимок: '+ str(user.num3)+ '\nКоличество нюдсов: '+ str(user.nums3), parse_mode='html')
                    elif dbworker.get_state(str(message.chat.id) + '_obl') == '5':
                        user = set_5(message, update=True)
                        
                        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                        markup.row("👤 Профиль", "🔧 Настройки")
                        markup.row("🔍 Поиск", "📝 Создать")
                        markup.row("🗂 Отзывы", "💎 PRIME")        
                        bot.send_message(message.chat.id, '🎉 Отзыв создан', parse_mode="html", reply_markup=markup)
                        bot.send_photo(message.chat.id, user.avatar12)
                        bot.send_message(message.chat.id,"-----------------Feedback-info-----------------\nИмя: <b>" + str(user.name4) +'</b> \nГород: <b>' + str(user.title4) +'</b> \nПревью: <b>' + str(user.link4) +'</b> \nОтзыв: <b>' + str(user.description4) +'</b>\n\nКоличество интимок: '+ str(user.num4)+ '\nКоличество нюдсов: '+ str(user.nums4), parse_mode='html')
            except Exception as err:
                msg = bot.send_message(message.chat.id, '❗️ Введите корректный адрес')
                bot.register_next_step_handler(msg, nuds)
                
        # Text messages
        @bot.message_handler(content_types=["text"])
        def text_messages(message, **kwargs):
            pprint(vars(message))
            user = get_user(message, update=True)
            if user.unban == True:
                if dbworker.get_state(str(message.chat.id) + '_wrkr') != '1':
                        if message.text == '1':
                            dbworker.set_state(str(message.chat.id) + '_obl', 2)
                            #user = godemode(message, update=True)
                            
                            #msg = bot.send_message(message.chat.id, '1')
                            #bot.register_next_step_handler(msg, gm)
                        if message.text == '🔧 Настройки':
                            keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
                            
        
    
                            key_ref = types.InlineKeyboardButton(text= "🤝 Реф. система", callback_data='ref'); #кнопка «Да»
                            key_rules = types.InlineKeyboardButton(text= "📜 Правила", callback_data='rules'); #кнопка «Да»
                            key_worker = types.InlineKeyboardButton(text="💎 Чат", url="https://t.me/kareltests", callback_data='worker'); #кнопка «Да»
                            key_wallet = types.InlineKeyboardButton(text= "💸 Канал с постами", url="https://t.me/karelrel"); #кнопка «Да»
                            keyboard.add(key_ref, key_rules)
                            keyboard.add(key_worker, key_wallet)
                            bot.send_message(message.chat.id, '🔧 <b>Настройки</b>\n\n🙈 Ваш ник: <b><a href="https://t.me/' + str(message.chat.username) + '">' + str(message.chat.username) + '</a></b>\n🤝 Пригласил: <b>' + str(dbworker.get_state(str(message.chat.id) + '_prigl'))+ '</b>',parse_mode="html", reply_markup=keyboard)

                        elif message.text == "👤 Профиль":
                            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                            markup.row("👤 Профиль", "🔧 Настройки")
                            markup.row("🔍 Поиск", "📝 Создать")
                            markup.row("🗂 Отзывы", "💎 PRIME")
                            bot.send_message(message.chat.id, "💸", reply_markup=markup)
                            keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
                            key_history = types.InlineKeyboardButton(text= "📋 История", callback_data='history'); #кнопка «Да»
                            keyboard.add(key_history);
                            if dbworker.get_state(str(message.chat.id) + '_status') == '3':
                                    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                                    markup.row("👤 Профиль", "🔧 Настройки")
                                    markup.row("🔍 Поиск", "📝 Создать")
                                    markup.row("🗂 Отзывы", "💎 PRIME")
                                    bot.send_message(message.chat.id, "💸", reply_markup=markup)
                                    keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
                                    
                                    key_history = types.InlineKeyboardButton(text= "📋 История", callback_data='history'); #кнопка «Да»
                                    
                                    keyboard.add(key_history);
                                    bot.send_message(message.chat.id, "👤 <b>Мой профиль</b>\n\n🆔 Ваш ID: <b>" + str(message.chat.id) + "</b>\n⭐️ Статус: <b>PRIME на 1 месяц</b>\n📆 С нами с : <b>"+ str(dbworker.get_state(str(message.chat.id) + '_end_date')) +"</b>",parse_mode="html", reply_markup=keyboard)
                            elif dbworker.get_state(str(message.chat.id) + '_status') == '4':
                                    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                                    markup.row("👤 Профиль", "🔧 Настройки")
                                    markup.row("🔍 Поиск", "📝 Создать")
                                    markup.row("🗂 Отзывы", "💎 PRIME")
                                    bot.send_message(message.chat.id, "💸", reply_markup=markup)
                                    keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
                                    
                                    key_history = types.InlineKeyboardButton(text= "📋 История", callback_data='history'); #кнопка «Да»
                                    
                                    keyboard.add(key_history);
                                    bot.send_message(message.chat.id, "👤 <b>Мой профиль</b>\n\n🆔 Ваш ID: <b>" + str(message.chat.id) + "</b>\n⭐️ Статус: <b>PRIME</b>\n📆 С нами с : <b>"+ str(dbworker.get_state(str(message.chat.id) + '_end_date')) +"</b>",parse_mode="html", reply_markup=keyboard)
                            else:
                                bot.send_message(message.chat.id, "👤 <b>Мой профиль</b>\n\n🆔 Ваш ID: <b>" + str(message.chat.id) + "</b>\n⭐️ Статус: <b>Обычный</b>\n📆 С нами с : <b>"+ str(dbworker.get_state(str(message.chat.id) + '_end_date')) +"</b>",parse_mode="html", reply_markup=keyboard)
                        elif message.text == "🔍 Поиск":
                                msg = bot.send_message(message.chat.id,'Введите ссылку на страницу вк, для просмотра отзыва бывших о человеке\n\n<i>❕ Огромная просьба - публикуйте отзывы о своих бывших, помогите людям не совершить ошибку, вместе мы поможем друг другу</i>', parse_mode='html')
                                bot.register_next_step_handler(msg, searh1) 
                        elif message.text == "💎 PRIME":
                            if dbworker.get_state(str(message.chat.id) + '_status') == '2':
                                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                                markup.row("💳 Приобрести","⬅️ Назад")
                                bot.send_message(message.chat.id, '💰Преемущество покупки прайм статуса:\nВы можете увидеть интимные фото с искаемого профиля или нюдсы\n🆔 Если вас слили или вы хотите защитится от слива, то приобретайте прайм статус - пользователи не смогут оставить отзыв, а так же уже существующие отзывы сотрутся\n<i>❕ Его можно приобрести навсегда всего за 100, или же на месяц пробную версию за 50 рублей</i>',parse_mode="Html", reply_markup=markup)
                            elif dbworker.get_state(str(message.chat.id) + '_status') == '3': 
                                if dbworker.get_state(str(message.chat.id) + '_time_test') >= str(datetime.today().strftime("%Y%m%d")):
                                    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                                    markup.row("💳 Доплатить", "⬅️ Назад")
                                    bot.send_message(message.chat.id, '💎 PRIME\nВы имеете прайм статус на 1 месяц\n<i>❕ Если хотите обновить аккаунт, то доплатите 50 рублей, пока не истек 1 месяц</i>',parse_mode="html", reply_markup=markup)
                                elif dbworker.get_state(str(message.chat.id) + '_time_test') <= str(datetime.today().strftime("%Y%m%d")):
                                    dbworker.set_state(str(message.chat.id) + '_time_test', 0)
                                    dbworker.set_state(str(message.chat.id) + '_status', 2)
                                    bot.send_message(message.chat.id, '💎 PRIME\nПрайм статус на 1 месяц закончился, теперь получить его навсегда, доплатив 50 рублей, не получится\n<i>❕ Если хотите обновить аккаунт, то доплатите 50 рублей, пока не истек 1 месяц</i>',parse_mode="html")
                            elif dbworker.get_state(str(message.chat.id) + '_status') == '4':
                                print(12)
                        elif message.text == "💳 Приобрести":
                            try:    
                                  
                                    price = 100 #Цена товара
                                    comment = api.bill(price)
                                    hide_markup = telebot.types.ReplyKeyboardRemove()
                                    bot.send_message(message.chat.id, 'Вам выставлен счет:\n'
                                    +'Сумма к оплате: 100 RUB\n'
                                    +'Страница оплаты QIWI : '
                                    +'QIWI кошелек: ' +'https://qiwi.com/payment/form/99999?extra[%27accountType%27]=nickname&extra[%27account%27]=EGORKARELIN\n'
                                    +'Комментарий платежа: \n<b>'+str(comment)+'</b>'
                                    +'\nУ вас есть 10 дней для оплаты транзакции, после истечения времени будут проблемы с оплатой из-за api qiwi, пожалуйста сохраните ключ из комментария', parse_mode="Html", reply_markup=hide_markup)
                                    api.start() #Запускает проверку
                                    while True: #Ну поняли
                                        if api.check(comment): #Если найдет комментарий то пропустит
                                            dbworker.set_state(str(message.chat.id) + '_status', 4)
                                            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                                            markup.row("👤 Профиль", "🔧 Настройки")
                                            markup.row("🔍 Поиск", "📝 Создать")
                                            markup.row("🗂 Отзывы", "💎 PRIME")
                                            dbworker.set_state(str(message.chat.id) + '_zak_dr', 1)
                                            dbworker.set_state(str(message.chat.id) + '_zak_price', price)
                                            bot.send_message(message.chat.id, "💸", reply_markup=markup)
                                            bot.send_message(message.chat.id, '❤️ Ваш статус обновлен на PRIME')
                                            msg = bot.send_message(message.chat.id, 'Отправьте ссылку с айди на ваш вк') 
                                            bot.register_next_step_handler(msg, upprime) 
                                            break

                                            sleep(1)
                                    
                                    api.stop()#Остановит проверку
                            except OverridingEx: #Ловлю ошибку
                                bot.send_message(message.chat.id, '⭐️ Если у вас высветилась эта ошибка, то напишите администратору @Eyaeje')
                        elif message.text == "💳 Доплатить":
                            try:    
                                if dbworker.get_state(str(message.chat.id) + '_status') == '3':    
                                    price = 50 #Цена товара
                                    comment = api.bill(price)
                                    hide_markup = telebot.types.ReplyKeyboardRemove()
                                    bot.send_message(message.chat.id, 'Вам выставлен счет:\n'
                                    +'Сумма к оплате: 50 RUB\n'
                                    +'Страница оплаты QIWI : '
                                    +'QIWI кошелек: ' +'https://qiwi.com/payment/form/99999?extra[%27accountType%27]=nickname&extra[%27account%27]=EGORKARELIN\n'
                                    +'Комментарий платежа: \n<b>'+str(comment)+'</b>'
                                    +'\nУ вас есть 10 дней для оплаты транзакции, после истечения времени будут проблемы с оплатой из-за api qiwi, пожалуйста сохраните ключ из комментария', parse_mode="Html", reply_markup=hide_markup)
                                    api.start() #Запускает проверку
                                    while True: #Ну поняли
                                        if api.check(comment): #Если найдет комментарий то пропустит
                                            dbworker.set_state(str(message.chat.id) + '_time_test', 0)
                                            dbworker.set_state(str(message.chat.id) + '_status', 4)
                                            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                                            markup.row("👤 Профиль", "🔧 Настройки")
                                            markup.row("🔍 Поиск", "📝 Создать")
                                            markup.row("🗂 Отзывы", "💎 PRIME")
                                            bot.send_message(message.chat.id, "💸", reply_markup=markup)
                                            bot.send_message(message.chat.id, '❤️ Ваш статус обновлен на PRIME')
                                            
                                            break

                                            sleep(1)
                                    
                                    api.stop()#Остановит проверку
                            except OverridingEx: #Ловлю ошибку
                                bot.send_message(message.chat.id, '⭐️ Если у вас высветилась эта ошибка, то напишите администратору @Eyaeje')
                        elif message.text == "⬅️ Назад":
                            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                            markup.row("👤 Профиль", "🔧 Настройки")
                            markup.row("🔍 Поиск", "📝 Создать")
                            markup.row("🗂 Отзывы", "💎 PRIME")  
                            bot.send_message(message.chat.id, "💸", reply_markup=markup)
                            keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
                            key_history = types.InlineKeyboardButton(text= "📋 История", callback_data='history'); #кнопка «Да»
                            keyboard.add(key_history);
                            if dbworker.get_state(str(message.chat.id) + '_status') == '3':
                                    bot.send_message(message.chat.id, "👤 <b>Мой профиль</b>\n\n🆔 Ваш ID: <b>" + str(message.chat.id) + "</b>\n⭐️ Статус: <b>PRIME на 1 месяц</b>\n📆 С нами с : <b>"+ str(dbworker.get_state(str(message.chat.id) + '_end_date')) +"</b>",parse_mode="html", reply_markup=keyboard)
                            elif dbworker.get_state(str(message.chat.id) + '_status') == '4':

                                    bot.send_message(message.chat.id, "👤 <b>Мой профиль</b>\n\n🆔 Ваш ID: <b>" + str(message.chat.id) + "</b>\n⭐️ Статус: <b>PRIME</b>\n📆 С нами с : <b>"+ str(dbworker.get_state(str(message.chat.id) + '_end_date')) +"</b>",parse_mode="html", reply_markup=keyboard)
                            else:
                                bot.send_message(message.chat.id, "👤 <b>Мой профиль</b>\n\n🆔 Ваш ID: <b>" + str(message.chat.id) + "</b>\n⭐️ Статус: <b>Обычный</b>\n📆 С нами с : <b>"+ str(dbworker.get_state(str(message.chat.id) + '_end_date')) +"</b>",parse_mode="html", reply_markup=keyboard)
                        elif message.text == "📝 Создать":
                            
                            msg = bot.send_message(message.chat.id, '<b>📝 Создание Отзыва</b>\n\n✏️ Введите имя:', parse_mode="HTML")
                            bot.register_next_step_handler(msg, create_twr) 


            elif dbworker.get_state(str(message.chat.id) + '_status') == '0':
                print(str(message.text))
            
            elif user.ban == True:
                bot.send_message(
                    message.chat.id,
                    '⛔ Вы заблокированны на данном сервисе ⛔',
                    parse_mode='Markdown'
                )
            return
                
            
            
            
        
        @bot.callback_query_handler(func=lambda call: True)
        def callback_worker(call):
            if call.data == "profile":
                keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
                key_history = types.InlineKeyboardButton(text= "📋 История", callback_data='history'); #кнопка «Да»
                keyboard.add(key_history);
                if dbworker.get_state(str(call.message.chat.id) + '_status') == '3':
                        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                        markup.row("👤 Профиль", "🔧 Настройки")
                        markup.row("🔍 Поиск", "📝 Создать")
                        markup.row("🗂 Отзывы", "💎 PRIME")
                        bot.send_message(call.message.chat.id, "💸", reply_markup=markup)
                        keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
                        
                        key_history = types.InlineKeyboardButton(text= "📋 История", callback_data='history'); #кнопка «Да»
                        
                        keyboard.add(key_history);
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="👤 <b>Мой профиль</b>\n\n🆔 Ваш ID: <b>" + str(call.message.chat.id) + "</b>\n⭐️ Статус: <b>PRIME на 1 месяц</b>\n📆 С нами с : <b>"+ str(dbworker.get_state(str(call.message.chat.id) + '_end_date')) +"</b>",parse_mode="html", reply_markup=keyboard)
                elif dbworker.get_state(str(call.message.chat.id) + '_status') == '4':
                        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                        markup.row("👤 Профиль", "🔧 Настройки")
                        markup.row("🔍 Поиск", "📝 Создать")
                        markup.row("🗂 Отзывы", "💎 PRIME")
                        bot.send_message(message.chat.id, "💸", reply_markup=markup)
                        keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
                        
                        key_history = types.InlineKeyboardButton(text= "📋 История", callback_data='history'); #кнопка «Да»
                        
                        keyboard.add(key_history);
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="👤 <b>Мой профиль</b>\n\n🆔 Ваш ID: <b>" + str(call.message.chat.id) + "</b>\n⭐️ Статус: <b>PRIME</b>\n📆 С нами с : <b>"+ str(dbworker.get_state(str(message.chat.id) + '_end_date')) +"</b>",parse_mode="html", reply_markup=keyboard)
                else:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="👤 <b>Мой профиль</b>\n\n🆔 Ваш ID: <b>" + str(call.message.chat.id) + "</b>\n⭐️ Статус: <b>Обычный</b>\n📆 С нами с : <b>"+ str(dbworker.get_state(str(call.message.chat.id) + '_end_date')) +"</b>",parse_mode="html", reply_markup=keyboard)
            elif call.data == "history":
                if dbworker.get_state(str(call.message.chat.id) + '_zak_dr') == '0': 
                    bot.send_message(call.message.chat.id, '❗️ Ваша история пополнений пуста')
                elif dbworker.get_state(str(call.message.chat.id) + '_zak_dr') == '1': 
                    bot.send_message(call.message.chat.id, "💳 Покупка прайм статуса за <b>"+ str(dbworker.get_state(str(message.chat.id) + '_zak_price')) + "</b>рублей",parse_mode="html")
            elif call.data == "rules":
                bot.send_message(call.message.chat.id, '<b>📜 Наши правила:</b>\n\n1. В чате запрещена реклама, флуд, спам, недопустимый контент\n2. Тут вы можете сливать и добавлять отзыв о своих бывших\n 3. Вы можете осуществлять поиск отзывов через ссылку в вк\n 4. Ставить интимки на основное фото для <b>разрешается</b>\n 5. Ставить обноженки на основное фото <b>запрещается</b> <i>❕(Карается баном)</i>\n 6. Оставлять в отзыве полные персональные данные <b>запрещено</b> <i>❕Имя не запрещается</i>', parse_mode="Html")
            elif call.data == "kard":
                bot.send_message(call.message.chat.id, '💳 Карта\n\n☘️ Номер:\n\n<i>❕ Используйте для предоплат, заранее предупредив ТС</i>', parse_mode="Html")
            
            elif call.data == "ref":
                bot.send_message(call.message.chat.id, '<b>🤝 Реферальная система</b>\n\n❤️ Чтобы пользователь стал вашим рефералом, при подаче заявки он должен указать ваш ID <b>'+ str(call.message.chat.id) +'</b>\n\n🧀 Также он может перейти по вашей реф. ссылке: <b>https://t.me/StepanovTestBot?start=' + str(call.message.chat.id) + '</b>\n\n<i>❕ Вы получите 💎 PRIME аккаунт на 1 месяц</i>', parse_mode="Html")
        
        bot.polling(none_stop=True)
