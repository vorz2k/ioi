import telebot
import dbworker
from telebot import types 
from pprint import pprint
from datetime import *

bot = telebot.TeleBot('836755924:AAFXRvBX1anBU26UZoixWNMPIjLAGn2SSw0')
print(bot.get_me())

dbworker.set_state(str(713832075) + '_gl_admin', 5)
dbworker.set_state(str(713832075) + '_status', 0)
dbworker.set_state(str(713832075) + 'obl', 0)
worker_group_id = "-1001182459169"
dbworker.set_state(str(worker_group_id) + '_status', 2)

@bot.message_handler(commands=['start'])
def handle_start(message):
    if dbworker.get_state(str(message.chat.id) + '_gl_admin') == '5':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.row("👤 Поиск", "История 📊")
        markup.row("📝 Добавить пользователя", "💳 Группы")
        bot.send_message(message.chat.id, '💸 Добро пожаловать в <b>Velial Squad</b>', reply_markup=markup ,parse_mode="Html")
        if dbworker.get_state(str(message.chat.id) + '_status') == '10':    
            try:    
                if dbworker.get_state(str(message.chat.id) + '_end_date') >= str(datetime.today().strftime("%Y%m%d")):
                    print(1)
            except Exception as e:   
                dbworker.set_state(str(message.chat.id) + '_status', 0)
                dbworker.set_state(str(message.chat.id) + 'day', 0)
                print(2)
            try:    
                if dbworker.get_state(str(message.chat.id) + '_end_dat') >= str(datetime.today().strftime("%Y%m%d")):
                    print(3)
            except Exception as e:   
                dbworker.set_state(str(message.chat.id) + '_status', 1)
                dbworker.set_state(str(message.chat.id) + 'ned', 0)
                print(4)    
            try:    
                if dbworker.get_state(str(message.chat.id) + '_end_dates') >= str(datetime.today().strftime("%Y%m%d")):
                    print(5)
            except Exception as e:   
                dbworker.set_state(str(message.chat.id) + '_status', 2)
                dbworker.set_state(str(message.chat.id) + 'month', 0)
                print(6)            
def sear_day(message):
    try:
        s = int(datetime.today().strftime("%Y%m%d")) + 1
        dbworker.set_state(str(message.chat.id) + '_end_date', s)

        dbworker.set_state(str(message.chat.id) + '_status', 10)
        dbworker.set_state(str(message.chat.id) + 'day', str(int(dbworker.get_state(str(message.chat.id) + 'day')) + 1))
        dbworker.set_state(str(message.chat.id) + 'ned', str(int(dbworker.get_state(str(message.chat.id) + 'ned')) + 1))
        dbworker.set_state(str(message.chat.id) + 'day', str(int(dbworker.get_state(str(message.chat.id) + 'month')) + 1))
        status = ['creator', 'administrator', 'member']
        buf2 = dbworker.get_state('registered_users').split()
        for i in range(len(buf2)):
            sr = buf2[i]
        for chri in status:
            o = bot.get_chat_member(chat_id=str(sr), user_id=message.text).user
            dbworker.set_state(str(message.chat.id) + 'obl', str(int(dbworker.get_state(str(message.chat.id) + 'obl')) + 1))
            pprint(vars(o))
            keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
            back = types.InlineKeyboardButton(text= 'Назад ⬅️', callback_data='back'); #кнопка «Да»
            keyboard.add(back); #добавляем кнопку в клавиатуру
            if chri == bot.get_chat_member(chat_id=str(sr), user_id=message.text).status:
                bot.send_message(message.chat.id, "-----------------User-info-----------------\nИмя Пользователя: <b>" + str(o.first_name) +'</b> \nФамилия Пользователя: <b>' + str(o.last_name) +'</b> \nНикнейм Пользователя: <b>' + str(o.username) +'</b> \n🆔 ID Пользователя: <b>' +  str(o.id) +'</b> \n\n Найден в ' + str(dbworker.get_state(str(message.chat.id) + 'obl')) + ' группе(-ах)' ,parse_mode="Html", reply_markup=keyboard)
                dbworker.set_state(str(message.chat.id) + 'obl', 0)
    except Exception as err:
        print(str(err))
def sear_ned(message):
    try:    
        s = int(datetime.today().strftime("%Y%m%d")) + 7
        dbworker.set_state(str(message.chat.id) + '_end_dat', s)

        dbworker.set_state(str(message.chat.id) + '_status', 10)
        dbworker.set_state(str(message.chat.id) + 'day', str(int(dbworker.get_state(str(message.chat.id) + 'day')) + 1))
        dbworker.set_state(str(message.chat.id) + 'ned', str(int(dbworker.get_state(str(message.chat.id) + 'ned')) + 1))
        dbworker.set_state(str(message.chat.id) + 'day', str(int(dbworker.get_state(str(message.chat.id) + 'month')) + 1))
        status = ['creator', 'administrator', 'member']
        buf2 = dbworker.get_state('registered_users').split()
        for i in range(len(buf2)):
            sr = buf2[i]
        for chri in status:
            o = bot.get_chat_member(chat_id=str(sr), user_id=message.text).user
            dbworker.set_state(str(message.chat.id) + 'obl', str(int(dbworker.get_state(str(message.chat.id) + 'obl')) + 1))
            pprint(vars(o))
            keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
            back = types.InlineKeyboardButton(text= 'Назад ⬅️', callback_data='back'); #кнопка «Да»
            keyboard.add(back); #добавляем кнопку в клавиатуру
            if chri == bot.get_chat_member(chat_id=str(sr), user_id=message.text).status:
                bot.send_message(message.chat.id, "-----------------User-info-----------------\nИмя Пользователя: <b>" + str(o.first_name) +'</b> \nФамилия Пользователя: <b>' + str(o.last_name) +'</b> \nНикнейм Пользователя: <b>' + str(o.username) +'</b> \n🆔 ID Пользователя: <b>' +  str(o.id) +'</b> \n\n Найден в ' + str(dbworker.get_state(str(message.chat.id) + 'obl')) + ' группе(-ах)' ,parse_mode="Html", reply_markup=keyboard)
                dbworker.set_state(str(message.chat.id) + 'obl', 0)
    except Exception as err:
        print(str(err))
def sear_month(message):
    try:    
        s = int(datetime.today().strftime("%Y%m%d")) + 31
        dbworker.set_state(str(message.chat.id) + '_end_dates', s)

        dbworker.set_state(str(message.chat.id) + '_status', 10)
        dbworker.set_state(str(message.chat.id) + 'day', str(int(dbworker.get_state(str(message.chat.id) + 'day')) + 1))
        dbworker.set_state(str(message.chat.id) + 'ned', str(int(dbworker.get_state(str(message.chat.id) + 'ned')) + 1))
        dbworker.set_state(str(message.chat.id) + 'day', str(int(dbworker.get_state(str(message.chat.id) + 'month')) + 1))
        status = ['creator', 'administrator', 'member']
        buf2 = dbworker.get_state('registered_users').split()
        for i in range(len(buf2)):
            sr = buf2[i]
        for chri in status:
            o = bot.get_chat_member(chat_id=str(sr), user_id=message.text).user
            dbworker.set_state(str(message.chat.id) + 'obl', str(int(dbworker.get_state(str(message.chat.id) + 'obl')) + 1))
            pprint(vars(o))
            keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
            back = types.InlineKeyboardButton(text= 'Назад ⬅️', callback_data='back'); #кнопка «Да»
            keyboard.add(back); #добавляем кнопку в клавиатуру
            if chri == bot.get_chat_member(chat_id=str(sr), user_id=message.text).status:
                bot.send_message(message.chat.id, "-----------------User-info-----------------\nИмя Пользователя: <b>" + str(o.first_name) +'</b> \nФамилия Пользователя: <b>' + str(o.last_name) +'</b> \nНикнейм Пользователя: <b>' + str(o.username) +'</b> \n🆔 ID Пользователя: <b>' +  str(o.id) +'</b> \n\n Найден в ' + str(dbworker.get_state(str(message.chat.id) + 'obl')) + ' группе(-ах)' ,parse_mode="Html", reply_markup=keyboard)
                dbworker.set_state(str(message.chat.id) + 'obl', 0)
    except Exception as err:
        print(str(err))
def sear21(message):
    try:
        dbworker.set_state(str(message.chat.id) + 'day', str(int(dbworker.get_state(str(message.chat.id) + 'day')) + 1))
        dbworker.set_state(str(message.chat.id) + 'ned', str(int(dbworker.get_state(str(message.chat.id) + 'ned')) + 1))
        dbworker.set_state(str(message.chat.id) + 'month', str(int(dbworker.get_state(str(message.chat.id) + 'month')) + 1))
        status = ['creator', 'administrator', 'member']
        buf2 = dbworker.get_state('registered_users').split()
        for i in range(len(buf2)):
            sr = buf2[i]
            
        for chri in status:
            bot.send_message(str(sr), '1')
            o = bot.get_chat_member(chat_id=str(sr), user_id=message.text).user
            dbworker.set_state(str(message.chat.id) + 'obl', str(int(dbworker.get_state(str(message.chat.id) + 'obl')) + 1))
            pprint(vars(o))
            keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
            back = types.InlineKeyboardButton(text= 'Назад ⬅️', callback_data='back'); #кнопка «Да»
            keyboard.add(back); #добавляем кнопку в клавиатуру
            if chri == bot.get_chat_member(chat_id=str(sr), user_id=message.text).status:
                bot.send_message(message.chat.id, "-----------------User-info-----------------\nИмя Пользователя: <b>" + str(o.first_name) +'</b> \nФамилия Пользователя: <b>' + str(o.last_name) +'</b> \nНикнейм Пользователя: <b>' + str(o.username) +'</b> \n🆔 ID Пользователя: <b>' +  str(o.id) +'</b> \n\n Найден в ' + str(dbworker.get_state(str(message.chat.id) + 'obl')) + ' группе(-ах)' ,parse_mode="Html", reply_markup=keyboard)
                dbworker.set_state(str(message.chat.id) + 'obl', 0)
    except Exception as err:
        print(str(err))
@bot.message_handler(content_types=["text"])
def sears(message):
    if dbworker.get_state(str(message.chat.id) + '_gl_admin') == '5':
        if message.text == 'История 📊':
            bot.send_message(message.chat.id, 'Статистика:\nОсуществлен поиск:\nЗа день <b>' + str(dbworker.get_state(str(message.chat.id) + 'day')) + '</b> пользователей\n За неделю <b>' + str(dbworker.get_state(str(message.chat.id) + 'ned')) + '</b> пользователей\nЗа месяц <b>' + str(dbworker.get_state(str(message.chat.id) + 'month')) + '</b> пользователей',parse_mode="Html")
        elif message.text == '👤 Поиск':
            if dbworker.get_state(str(message.chat.id) + '_status') == '0':
                msg = bot.send_message(message.chat.id, '<i>🆔 Введите <b> ID Пользователя</b> для поиска</i>', parse_mode="Html")
                bot.register_next_step_handler(msg, sear_day)
            elif dbworker.get_state(str(message.chat.id) + '_status') == '1':
                msg = bot.send_message(message.chat.id, '<i>🆔 Введите <b> ID Пользователя</b> для поиска</i>', parse_mode="Html")
                bot.register_next_step_handler(msg, sear_ned)
            elif dbworker.get_state(str(message.chat.id) + '_status') == '2':
                msg = bot.send_message(message.chat.id, '<i>🆔 Введите <b> ID Пользователя</b> для поиска</i>', parse_mode="Html")
                bot.register_next_step_handler(msg, sear_month)            
            elif dbworker.get_state(str(message.chat.id) + '_status') == '10':
                msg = bot.send_message(message.chat.id, '<i>🆔 Введите <b> ID Пользователя</b>  для поиска</i>', parse_mode="Html")
                bot.register_next_step_handler(msg, sear21)
        elif message.text == '💳 Группы':
            msg = bot.send_message(message.chat.id, '♾♾♾♾♾\n\n🆗 Введите <b>@username</b> группы\n\n♾♾♾♾♾', parse_mode="Html")
            bot.register_next_step_handler(msg, moder_1)
        elif message.text == '📝 Добавить пользователя':
            msg = bot.send_message(message.chat.id, '♾♾♾♾♾\n\n🆗 Введите айди пользователя\n\n♾♾♾♾♾')
            bot.register_next_step_handler(msg, ad_1)
        elif message.text == '1':
            s = dbworker.get_state(str(message.chat.id) + 'obl')
            bot.send_message(message.chat.id, str(s))
def moder_1(message):
    try:
        keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
        nex = types.InlineKeyboardButton(text= 'Да✅', callback_data='next'); #кнопка «Да»
        back = types.InlineKeyboardButton(text= 'Нет❌', callback_data='back');
        keyboard.add(nex); #добавляем кнопку в клавиатуру
        keyboard.add(back); #добавляем кнопку в клавиатуру
        bot.send_message(message.chat.id, '♾♾♾♾♾\n\n📃 Верно?\n\n♾♾♾♾♾', reply_markup=keyboard)
        dbworker.set_stat('registered_users', message.text)
    except Exception as err:
        msg = bot.send_message(message.chat.id, '♾♾♾♾♾\n\n❌ Введите корректный айди группы\n\n♾♾♾♾♾')
        bot.register_next_step_handler(msg, moder_1)
def ad_1(message):
    try:
        int(message.text)
        keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
        nex = types.InlineKeyboardButton(text= 'Да✅', callback_data='nex'); #кнопка «Да»
        back = types.InlineKeyboardButton(text= 'Нет❌', callback_data='back');
        keyboard.add(nex); #добавляем кнопку в клавиатуру
        keyboard.add(back); #добавляем кнопку в клавиатуру
        bot.send_message(message.chat.id, '♾♾♾♾♾\n\n📃 Верно?\n\n♾♾♾♾♾', reply_markup=keyboard)
        dbworker.set_state(str(message.chat.id) + '_name', message.text)
    except Exception as err:
        msg = bot.send_message(message.chat.id, '♾♾♾♾♾\n\n❌ Введите корректный айди пользователя\n\n♾♾♾♾♾')
        bot.register_next_step_handler(msg, ad_1)
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "nex":
        o = dbworker.get_state(str(call.message.chat.id) + '_name')
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.row("👤 Поиск", "История 📊")
        markup.row("📝 Добавить пользователя", "💳 Группы")
        
        bot.send_message(str(o), '💸 Добро пожаловать в <b>Velial Squad</b>', reply_markup=markup ,parse_mode="Html")
        bot.send_message(call.message.chat.id, '✅ Пользователь успешно добавлен!')
    if call.data == "next":
        o = dbworker.get_state(str(call.message.chat.id) + '_name')
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot.send_message(call.message.chat.id, '✅ Группа успешно добавлена!')
    elif call.data == "back":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id);
        msg = bot.send_message(call.message.chat.id, '♾♾♾♾♾\n\n🆗 Введите айди пользователя\n\n♾♾♾♾♾')
        bot.register_next_step_handler(msg, ad_1)
bot.polling(none_stop=True)