import xadmin

from .models import City, CourseOrg, Teacher


class CityAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name']
    list_filter = ['name', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'bookmark_num', 'address', 'city', 'add_time']
    search_fields = ['name', 'bookmark_num', 'address', 'description', 'city']
    list_filter = ['name', 'bookmark_num', 'address', 'city', 'add_time']


class TeacherAdmin(object):
    list_display = ['name', 'org', 'work_years', 'bookmark_num', 'style', 'add_time']
    search_fields = ['name', 'org', 'style']
    list_filter = ['name', 'org', 'work_years', 'bookmark_num', 'style', 'add_time']


xadmin.site.register(City, CityAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
