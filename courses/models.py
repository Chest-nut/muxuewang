from datetime import datetime

from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, verbose_name='课程描述')
    detail = models.TextField(verbose_name='课程详情')
    degree = models.CharField(max_length=2,
                              choices=(('cj','初级'), ('zj','中级'), ('gj','高级')),
                              default='cj')
    learning_hours = models.SmallIntegerField(default=0, verbose_name='学习时长（分钟）')
    student_num = models.IntegerField(verbose_name='学习人数')
    bookmark_num = models.IntegerField(verbose_name='收藏人数')
    image = models.ImageField(max_length=100,
                              upload_to='courses/image./%/Y%m',
                              verbose_name='封面图')
    click_num = models.IntegerField(default=0)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name


class Chapter(models.Model):
    course = models.ForeignKey(Course)
    name = models.CharField(max_length=100)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name


class video(models.Model):
    chapter = models.ForeignKey(Chapter)
    name = models.CharField(max_length=100)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name


class CourseMaterial(models.Model):
    course = models.ForeignKey(Course)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='courses/resource/%Y/%m', max_length=100)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '课程资料'
        verbose_name_plural = verbose_name