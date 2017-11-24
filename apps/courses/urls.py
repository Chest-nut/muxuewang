from django.conf.urls import url

from courses.views import CourseList

urlpatterns = [
    url(r'^list/$', CourseList.as_view(), name='course_list'),
]