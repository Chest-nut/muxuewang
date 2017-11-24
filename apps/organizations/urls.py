from django.conf.urls import url

from organizations.views import OrgList, AddUserAsk, OrgCourses, \
    OrgDesc, OrgTeachers, AddOrgFav

urlpatterns = [
    url(r'^list/$', OrgList.as_view(), name='orglist'),
    url(r'^add_ask/$', AddUserAsk.as_view(), name='add_ask'),

    url(r'^courses/(?P<org_id>\d+)$', OrgCourses.as_view(), name='org_courses'),
    url(r'^teachers/(?P<org_id>\d+)$', OrgTeachers.as_view(), name='org_teachers'),
    url(r'^desc/(?P<org_id>\d+)$', OrgDesc.as_view(), name='org_desc'),
    url(r'^add_fav/$', AddOrgFav.as_view(), name='add_fav'),
]