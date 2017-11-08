import xadmin

from .models import EmailVerificationCode, Banner


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