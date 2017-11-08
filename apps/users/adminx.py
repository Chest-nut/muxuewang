import xadmin
from xadmin import views

from .models import EmailVerificationCode, Banner


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = '慕学网后台管理系统'
    site_footer = '慕学网'
    menu_style = 'accordion'


class EmailVerificationCodeAdmin(object):
    list_display = ['code', 'email', 'sent_type', 'send_time']
    search_fields = ['code', 'email', 'sent_type']
    list_filter = ['code', 'email', 'sent_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'order', 'add_time']
    search_fields = ['title', 'image', 'url', 'order']
    list_filter = ['title', 'image', 'url', 'order', 'add_time']


xadmin.site.register(EmailVerificationCode, EmailVerificationCodeAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)