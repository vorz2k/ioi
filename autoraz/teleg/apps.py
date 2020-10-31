import telebot

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TelegramConfig(AppConfig):
    name = 'teleg'
    verbose_name = _('Telegram')
    label = 'telegram'
    bot = None
    
    def ready(self):

        from .registry import registry

        try:
            api_key = '836755924:AAFXRvBX1anBU26UZoixWNMPIjLAGn2SSw0'
            bot = telebot.TeleBot(api_key, threaded=False, skip_pending=False)
            registry(bot)
        except:
            pass
