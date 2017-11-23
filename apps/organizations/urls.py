from django.conf.urls import url

from organizations.views import OrgList, AddUserAsk

urlpatterns = [
    url(r'^list/$', OrgList.as_view(), name='orglist'),
    url(r'^add_ask/$', AddUserAsk.as_view(), name='add_ask'),
]