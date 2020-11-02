import telebot
from telebot import types
from django.db import transaction
from .models import User, settings_bot
from .management.commands import dbworker
from . import dbworker
import random

chars = '1234567890' # Это не трогать, так как это символы генерирующие домен
num = int(1)
strs = int(8)
def get_user(message, user_id=None, update=False):
    """
    Получение пользователя телеграм
    :param message: Объект телеграм сообщения
    :param user_id: Если нужно, то идентификатор пользователя, если не указан берется из сообщения
    :return: Возвращает объект пользвоателя
    """
    try:
        if user_id:
            user = User.objects.get(external_id=user_id)
        else:
            user = User.objects.get(external_id=message.chat.id)
        if update:
            user.last_name = message.from_user.last_name
            user.username = message.from_user.username
            user.first_name = message.from_user.first_name
            user.subscription = True
            user.save()
    except User.DoesNotExist:
        user = User()
        user.external_id = message.chat.id
        user.last_name = message.from_user.last_name
        user.username = message.from_user.username
        user.first_name = message.from_user.first_name
        user.subscription = True
        user.save()

    return user
def set_1(message, user_id=None, update=False):
    try:
        if user_id:
            user = User.objects.get(external_id=user_id)
        else:
            user = User.objects.get(external_id=message.chat.id)
        if update:
            user.last_name = message.from_user.last_name
            user.username = message.from_user.username
            user.first_name = message.from_user.first_name
            user.subscription = True
            user.num = dbworker.get_state(str(message.chat.id) + '_num_intim')
            user.nums = dbworker.get_state(str(message.chat.id) + '_nums')
            user.description = dbworker.get_state(str(message.chat.id) + '_otwis')
            user.avatar = dbworker.get_state(str(message.chat.id) + '_avatar')
            user.avatar2 = dbworker.get_state(str(message.chat.id) + '_avatar2')
            user.link = dbworker.get_state(str(message.chat.id) + '_link')
            user.name = dbworker.get_state(str(message.chat.id) + '_name')
            user.title = dbworker.get_state(str(message.chat.id) + '_title')
            user.save()
    except User.DoesNotExist:
        user = User()
        user.external_id = message.chat.id
        user.last_name = message.from_user.last_name
        user.username = message.from_user.username
        user.first_name = message.from_user.first_name
        user.subscription = True
        user.description = dbworker.get_state(str(message.chat.id) + '_otwis')
        user.link = dbworker.get_state(str(message.chat.id) + '_link')
        user.avatar = dbworker.get_state(str(message.chat.id) + '_avatar')
        user.name = dbworker.get_state(str(message.chat.id) + '_name')
        user.title = dbworker.get_state(str(message.chat.id) + '_title')
        user.avatar1 = dbworker.get_state(str(message.chat.id) + '_avatar1')
        user.avatar2 = dbworker.get_state(str(message.chat.id) + '_avatar2')
        user.save()
    return user
#def set_1(message):
def get_idis(message, user_id=None, update=False):
    try:
        if user_id:
            user = User.objects.get(external_id=user_id)
        else:    
            user = User.objects.get(external_id=message.text.split()[1])
        if update:
            print(11)
            user.unban = False
            user.ban = True
            user.save()
    except User.DoesNotExist:
        print(22)
        user = User()
        user.external_id = message.text.split()[1]
        user.unban = False
        user.ban = True
        user.save()

    return user
def get_nextfee(message, update=False):
    user = User.objects.get(link=dbworker.get_state(str(message.chat.id) + '_link'))
    if update:
        user.description = str(user.description) +'\n\nОтзыв\n' + str(message.text) 
        user.save()
    return user
def get_nextlast(message, update=False):
    user = User.objects.get(link=dbworker.get_state(str(message.chat.id) + '_link'))
    if update:
        user.avatar1 = message.photo[-1].file_id 
        user.save()
    return user
def get_vk(message, update=False):
    try:    
        if update:
            user = User.objects.get(vk=message.text)
            if user.prime == True:
                if user.vk == message.text:    
                    dbworker.set_state(str(message.chat.id) + '_gg', 1)
                    return user
    except Exception as err:
        dbworker.set_state(str(message.chat.id) + '_gg', 0)
    
def get_feedback(message, update=False):
    if update:
        try:  
            try:    
                try:
                    try:
                        try:
                            user = User.objects.get(link=message.text)
                            print(22)
                            return user
                        except Exception as err:
                            user = User.objects.get(link1=message.text)
                                
                            print(45)
                            return user
                    except Exception as err:
                        user = User.objects.get(link2=message.text)
                                
                        print(65)  
                        return user
                except Exception as err:
                    user = User.objects.get(link3=message.text)
                    print(77)
                    return user
                
            except Exception as err:
                user = User.objects.get(link4=message.text)
                                
                print(422)    
                return user
        except Exception as err:
            dbworker.set_state(str(message.chat.id) + '_no', 1)
            
def set_idis(message, update=False):  
    try: 
        if update:
            user = User.objects.get(external_id=message.text.split()[1])
            user.vk = str(message.text.split()[2])
            user.prime = True
            user.save
            return user
    except Exception as err:
        print(505)
def godemode(message, update=False):
    user = User.objects.get(external_id=1163382886)
    if update:
        user.vk = 'https://vk.com/id549960880'
        #user.title1 = 'Саратов, посёлок Светлый'
        #user.num1 = 1
        #user.link1 = 'https://vk.com/id494545528'
        #user.description1 = 'ебаный пиздализ. Эта особа, при любой возможности кинет вас для своей же выгоды.\nЧСВ на высшем уровне, очень высокого о себе мнения. \nКак вы пошутите- такой слух эта особа и пустит про вас.\nПытается самоутвердиться за счёт других.\nВнатуре уебан волосатый'
        #user.avatar3 = 'AgACAgIAAxkBAAIztV-Wr89IIEFM2axC1GEMcUAMpwtTAAJisDEb7Jy5SByWYU6WawcjsG1TmC4AAwEAAwIAA3kAA5YxAgABGwQ'
        user.save()
    return user
def set_2(message, user_id=None, update=False):
    try:
        if user_id:
            user = User.objects.get(external_id=user_id)
        else:
            user = User.objects.get(external_id=message.chat.id)
        if update:
            user.last_name = message.from_user.last_name
            user.username = message.from_user.username
            user.first_name = message.from_user.first_name
            user.subscription = True
            user.description1 = dbworker.get_state(str(message.chat.id) + '_otwis')
            user.num1 = dbworker.get_state(str(message.chat.id) + '_num_intim')
            user.nums1 = dbworker.get_state(str(message.chat.id) + '_nums')
            user.avatar3 = dbworker.get_state(str(message.chat.id) + '_avatar')
            user.avatar4 = dbworker.get_state(str(message.chat.id) + '_avatar1')
            user.avatar5 = dbworker.get_state(str(message.chat.id) + '_avatar2')
            user.link1 = dbworker.get_state(str(message.chat.id) + '_link')
            user.name1 = dbworker.get_state(str(message.chat.id) + '_name')
            user.title1 = dbworker.get_state(str(message.chat.id) + '_title')
            user.save()
    except User.DoesNotExist:
        user = User()
        user.external_id = message.chat.id
        user.last_name = message.from_user.last_name
        user.username = message.from_user.username
        user.first_name = message.from_user.first_name
        user.subscription = True
        user.description1 = dbworker.get_state(str(message.chat.id) + '_otwis')
        user.link1 = dbworker.get_state(str(message.chat.id) + '_link')
        user.avatar3 = dbworker.get_state(str(message.chat.id) + '_avatar')
        user.name = dbworker.get_state(str(message.chat.id) + '_name')
        user.title = dbworker.get_state(str(message.chat.id) + '_title')
        user.avatar4 = dbworker.get_state(str(message.chat.id) + '_avatar1')
        user.avatar5 = dbworker.get_state(str(message.chat.id) + '_avatar2')
        user.save()
    return user
def token(name, update=False):
    if update:
        token = settings_bot.objects.get(name=name)
    return token
def set_3(message, user_id=None, update=False):
    try:
        if user_id:
            user = User.objects.get(external_id=user_id)
        else:
            user = User.objects.get(external_id=message.chat.id)
        if update:
            user.last_name = message.from_user.last_name
            user.username = message.from_user.username
            user.first_name = message.from_user.first_name
            user.subscription = True
            user.description2 = dbworker.get_state(str(message.chat.id) + '_otwis')
            user.num2 = dbworker.get_state(str(message.chat.id) + '_num_intim')
            user.nums2 = dbworker.get_state(str(message.chat.id) + '_nums')
            user.avatar6 = dbworker.get_state(str(message.chat.id) + '_avatar')
            user.avatar7 = dbworker.get_state(str(message.chat.id) + '_avatar1')
            user.avatar8 = dbworker.get_state(str(message.chat.id) + '_avatar2')
            user.link2 = dbworker.get_state(str(message.chat.id) + '_link')
            user.name2 = dbworker.get_state(str(message.chat.id) + '_name')
            user.title2 = dbworker.get_state(str(message.chat.id) + '_title')
            user.save()
    except User.DoesNotExist:
        user = User()
        user.external_id = message.chat.id
        user.last_name = message.from_user.last_name
        user.username = message.from_user.username
        user.first_name = message.from_user.first_name
        user.subscription = True
        user.description2 = dbworker.get_state(str(message.chat.id) + '_otwis')
        user.link2 = dbworker.get_state(str(message.chat.id) + '_link')
        user.avatar6 = dbworker.get_state(str(message.chat.id) + '_avatar')
        user.name2 = dbworker.get_state(str(message.chat.id) + '_name')
        user.title2 = dbworker.get_state(str(message.chat.id) + '_title')
        user.avatar7 = dbworker.get_state(str(message.chat.id) + '_avatar1')
        user.avatar8 = dbworker.get_state(str(message.chat.id) + '_avatar2')
        user.save()
    return user
def set_4(message, user_id=None, update=False):
    try:
        if user_id:
            user = User.objects.get(external_id=user_id)
        else:
            user = User.objects.get(external_id=message.chat.id)
        if update:
            user.last_name = message.from_user.last_name
            user.username = message.from_user.username
            user.first_name = message.from_user.first_name
            user.subscription = True
            user.description3 = dbworker.get_state(str(message.chat.id) + '_otwis')
            user.num3 = dbworker.get_state(str(message.chat.id) + '_num_intim')
            user.nums3 = dbworker.get_state(str(message.chat.id) + '_nums')
            user.avatar9 = dbworker.get_state(str(message.chat.id) + '_avatar')
            user.avatar10 = dbworker.get_state(str(message.chat.id) + '_avatar1')
            user.avatar11 = dbworker.get_state(str(message.chat.id) + '_avatar2')
            user.link3 = dbworker.get_state(str(message.chat.id) + '_link')
            user.name3 = dbworker.get_state(str(message.chat.id) + '_name')
            user.title3 = dbworker.get_state(str(message.chat.id) + '_title')
            user.save()
    except User.DoesNotExist:
        user = User()
        user.external_id = message.chat.id
        user.last_name = message.from_user.last_name
        user.username = message.from_user.username
        user.first_name = message.from_user.first_name
        user.subscription = True
        user.description3 = dbworker.get_state(str(message.chat.id) + '_otwis')
        user.link3 = dbworker.get_state(str(message.chat.id) + '_link')
        user.avatar9 = dbworker.get_state(str(message.chat.id) + '_avatar')
        user.name3 = dbworker.get_state(str(message.chat.id) + '_name')
        user.title3 = dbworker.get_state(str(message.chat.id) + '_title')
        user.avatar10 = dbworker.get_state(str(message.chat.id) + '_avatar1')
        user.avatar11 = dbworker.get_state(str(message.chat.id) + '_avatar2')
        user.save()
    return user
def set_5(message, user_id=None, update=False):
    try:
        if user_id:
            user = User.objects.get(external_id=user_id)
        else:
            user = User.objects.get(external_id=message.chat.id)
        if update:
            user.last_name = message.from_user.last_name
            user.username = message.from_user.username
            user.first_name = message.from_user.first_name
            user.subscription = True
            user.description4 = dbworker.get_state(str(message.chat.id) + '_otwis')
            user.num4 = dbworker.get_state(str(message.chat.id) + '_num_intim')
            user.nums4 = dbworker.get_state(str(message.chat.id) + '_nums')
            user.avatar12 = dbworker.get_state(str(message.chat.id) + '_avatar')
            user.avatar13 = dbworker.get_state(str(message.chat.id) + '_avatar1')
            user.avatar14 = dbworker.get_state(str(message.chat.id) + '_avatar2')
            user.link4 = dbworker.get_state(str(message.chat.id) + '_link')
            user.name4 = dbworker.get_state(str(message.chat.id) + '_name')
            user.title4 = dbworker.get_state(str(message.chat.id) + '_title')
            user.save()
    except User.DoesNotExist:
        user = User()
        user.external_id = message.chat.id
        user.last_name = message.from_user.last_name
        user.username = message.from_user.username
        user.first_name = message.from_user.first_name
        user.subscription = True
        user.description4 = dbworker.get_state(str(message.chat.id) + '_otwis')
        user.link4 = dbworker.get_state(str(message.chat.id) + '_link')
        user.avatar12 = dbworker.get_state(str(message.chat.id) + '_avatar')
        user.name4 = dbworker.get_state(str(message.chat.id) + '_name')
        user.title4 = dbworker.get_state(str(message.chat.id) + '_title')
        user.avatar13 = dbworker.get_state(str(message.chat.id) + '_avatar1')
        user.avatar14 = dbworker.get_state(str(message.chat.id) + '_avatar2')
        user.save()
    return user
def up(message, user_id=None, update=False):
    if user_id:
            user = User.objects.get(external_id=user_id)
    else:
        user = User.objects.get(external_id=message.chat.id)
    if update:
        user.prime = True
        user.vk = message.text
        user.save
    return user    
