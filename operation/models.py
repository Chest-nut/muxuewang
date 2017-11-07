from datetime import datetime

from django.db import models

from courses.models import Course
from users.models import UserInfo

# Create your models here.


class UserAsk(models.Model):
    username = models.CharField(max_length=20)
    mobile = models.CharField(max_length=11, null=True)
    course_name = models.CharField(max_length=50)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name


class CourseComment(models.Model):
    user = models.ForeignKey(UserInfo, verbose_name='评论用户')
    course = models.ForeignKey(Course)
    comment = models.CharField(max_length=200)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '课程评论'
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserInfo)
    fav_id = models.IntegerField(verbose_name='学习人数')
    fav_type = models.SmallIntegerField(choices=((1,'课程'), (2,'机构'), (3,'讲师')))
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name='接收用户')
    message = models.CharField(max_length=500)
    has_read = models.BooleanField(default=False)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(UserInfo)
    course = models.ForeignKey(Course)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '用户所学课程'
        verbose_name_plural = verbose_name
