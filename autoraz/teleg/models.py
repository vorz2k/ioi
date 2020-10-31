from django.db import models
from django.utils.translation import ugettext_lazy as _

class User(models.Model):
    external_id = models.CharField("Telegram_id", max_length=255, blank=True, null=True, unique=True)
    last_name = models.CharField(_('Last name'), max_length=255, blank=True, null=True)
    first_name = models.CharField(_('First name'), max_length=255, blank=True, null=True)
    username = models.CharField(_("username"),max_length=255)
    ban = models.BooleanField('Is Banned', default=False)
    unban = models.BooleanField('Is UnBanned', default=True)
    subscription = models.BooleanField('subscription', default=False)
    vk = models.URLField()
    prime = models.BooleanField('PRIME', default=False)
    
    link = models.URLField()
    title = models.CharField(u'Город', max_length=250)
    name = models.TextField(u'Имя', blank=True, default='')
    description = models.TextField(u'Описание', blank=True, default='')
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    num = models.TextField(u'Кол. интимок', blank=True, default='')
    nums = models.TextField(u'Кол. нюдсов', blank=True, default='')
    avatar = models.TextField(u'Код превью', blank=True, default='')
    avatar1 = models.TextField(u'Код интимки', blank=True, default='')
    avatar2 = models.TextField(u'Код обнаж.', blank=True, default='')

    link1 = models.URLField()
    title1 = models.CharField(u'Город', max_length=250)
    name1 = models.TextField(u'Имя', blank=True, default='')
    description1 = models.TextField(u'Описание', blank=True, default='')
    num1 = models.TextField(u'Кол. интимок', blank=True, default='')
    nums1 = models.TextField(u'Кол. нюдсов', blank=True, default='')
    avatar3 = models.TextField(u'Код превью', blank=True, default='')
    avatar4 = models.TextField(u'Код интимки', blank=True, default='')
    avatar5 = models.TextField(u'Код обнаж.', blank=True, default='')
    create_date1 = models.DateTimeField(auto_now_add=True)
    update_date1 = models.DateTimeField(auto_now=True)
    

    link2 = models.URLField()
    title2 = models.CharField(u'Город', max_length=250)
    name2 = models.TextField(u'Имя', blank=True, default='')
    description2 = models.TextField(u'Описание', blank=True, default='')
    num2 = models.TextField(u'Кол. интимок', blank=True, default='')
    nums2 = models.TextField(u'Кол. нюдсов', blank=True, default='')
    avatar6 = models.TextField(u'Код превью', blank=True, default='')
    avatar7 = models.TextField(u'Код интимки', blank=True, default='')
    avatar8 = models.TextField(u'Код обнаж.', blank=True, default='')
    create_date2 = models.DateTimeField(auto_now_add=True)
    update_date2 = models.DateTimeField(auto_now=True)
    
    link3 = models.URLField()
    title3 = models.CharField(u'Город', max_length=250)
    name3 = models.TextField(u'Имя', blank=True, default='')
    description3 = models.TextField(u'Описание', blank=True, default='')  
    num3 = models.TextField(u'Кол. интимок', blank=True, default='')
    nums3 = models.TextField(u'Кол. нюдсов', blank=True, default='')
    avatar9 = models.TextField(u'Код превью', blank=True, default='')
    avatar10 = models.TextField(u'Код интимки', blank=True, default='')
    avatar11 = models.TextField(u'Код обнаж.', blank=True, default='')  
    create_date3 = models.DateTimeField(auto_now_add=True)
    update_date3 = models.DateTimeField(auto_now=True)
    

    link4 = models.URLField()
    title4 = models.CharField(u'Город', max_length=250)
    name4 = models.TextField(u'Имя', blank=True, default='')
    description4 = models.TextField(u'Описание', blank=True, default='')
    num4 = models.TextField(u'Кол. интимок', blank=True, default='')
    nums4 = models.TextField(u'Кол. нюдсов', blank=True, default='')
    avatar12 = models.TextField(u'Код превью', blank=True, default='')
    avatar13 = models.TextField(u'Код интимки', blank=True, default='')
    avatar14 = models.TextField(u'Код обнаж.', blank=True, default='')
    create_date4 = models.DateTimeField(auto_now_add=True)
    update_date4 = models.DateTimeField(auto_now=True)
  

    
    

    
    def __str__(self):
        return f'#{self.external_id} {self.username}'
    
    class Meta:
        db_table = 'telegram_users'
        verbose_name='Профиль'
        verbose_name_plural = 'Профили'
class settings_bot(models.Model): 
    token_bot = models.TextField(u'Токен бота', blank=True, default='')
    name = models.TextField(u'Имя', blank=True, default='karel')
    class Meta:
        db_table = 'telegram_token'
        verbose_name='Настройку'
        verbose_name_plural = 'Настройки'
'''class Message(models.Model):
    profile = models.ForeignKey(
        to='teleg.User',
        verbose_name='Профиль',
        on_delete=models.PROTECT,
    )
    text = models.TextField(
        verbose_name='Сообщение',
    )
    createt_at = models.DateTimeField(
        verbose_name='Время получения',
        auto_now_add=True,
    )

    def __str__(self):
        return f'Сообщение {self.pk} {self.profile}'
    
    class Meta:
        verbose_name='Сообщение'
        verbose_name_plural = 'Сообщения'''