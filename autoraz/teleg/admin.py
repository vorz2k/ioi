from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import User, settings_bot
from .forms import UserForm

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'external_id', 'last_name', 'first_name', 'username', 'ban', 'subscription',)
    list_display_links = ('username', 'external_id',)
    list_filter = ("ban",)
    #readonly_fields = ('name', 'external_id',)
    list_editable = ("subscription", "ban", )
    search_fields = ('external_id', 'username', 'link', 'link1', 'link2', 'link3', 'link4',)
    actions= ["prr","baned", "unbaned"]
    form = UserForm
    def prr(self, request, queryset):
        ##Разбанить пользователя
        row_update = queryset.update(prime=True)
        
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
            self.message_user(request, f"{message_bit}")
    prr.short_description = "Выдать прайм"
    prr.allowed_permissions = ('change', )

    def baned(self, request, queryset):
        ##Забанить пользователя
        row_updat = queryset.update(unban=False)
        row_update = queryset.update(ban=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
            self.message_user(request, f"{message_bit}")
    def unbaned(self, request, queryset):
        ##Разбанить пользователя
        row_updat = queryset.update(unban=True)
        row_update = queryset.update(ban=False)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
    unbaned.short_description = "Разбанить"
    unbaned.allowed_permissions = ('change', )

    baned.short_description = "Забанить"
    baned.allowed_permissions = ('change', )
    fieldsets = (
        (None, {
            'fields': ('username', 'first_name', 'last_name', 'external_id', 'subscription','prime', 'vk',)
        }),
        (_('first_anket'), {
            'fields': ('link', 'title', 'name','description','num' ,'nums' ,'avatar' ,'avatar1','avatar2',  )
        }),
        (_('second_anket'), {
            'fields': ('link1', 'title1', 'name1','description1','num1' ,'nums1', 'avatar3' ,'avatar4','avatar5', )
        }),
        (_('third_anket'), {
            'fields': ('link2', 'title2', 'name2','description2','num2' ,'nums2' ,'avatar6' ,'avatar7','avatar8',)
        }),
        (_('fourth_anket'), {
            'fields': ('link3', 'title3', 'name3','description3','num3' ,'nums3' ,'avatar9' ,'avatar10','avatar11', )
        }),
        (_('fifth_anket'), {
            'fields': ('link4', 'title4', 'name4','description4','num4' ,'nums4' ,'avatar12' ,'avatar13','avatar14', )
        }),
    )
class UserMessage(admin.ModelAdmin):
    list_display = ('id', 'profile', 'text', 'createt_at')
@admin.register(settings_bot)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('token_bot', 'name')
    #def get_queryset(self, request):
        #return