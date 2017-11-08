import xadmin

from .models import Course, Chapter, video, CourseMaterial


class CourseAdmin(object):
    list_display = ['name', 'degree', 'learning_hours', 'student_num', 'add_time']
    search_fields = ['name', 'degree', 'description', 'detail']
    list_filter = ['name', 'degree', 'learning_hours', 'student_num', 'add_time']


class ChapterAdmin(object):
    list_display = ['course', 'name','add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name','add_time']


class videoAdmin(object):
    list_display = ['chapter', 'name', 'add_time']
    search_fields = ['chapter', 'name']
    list_filter = ['chapter__name', 'name', 'add_time']


class CourseMaterialAdmin(object):
    list_display = ['course', 'name', 'file', 'add_time']
    search_fields = ['course', 'name', 'file']
    list_filter = ['course__name', 'name', 'file', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Chapter, ChapterAdmin)
xadmin.site.register(video, videoAdmin)
xadmin.site.register(CourseMaterial, CourseMaterialAdmin)