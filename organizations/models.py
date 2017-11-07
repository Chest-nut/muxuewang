from datetime import datetime

from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=20)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, verbose_name='机构描述')
    bookmark_num = models.IntegerField(verbose_name='收藏人数')
    image = models.ImageField(max_length=100,
                              upload_to='org/image/%Y/%m',
                              verbose_name='封面图')
    click_num = models.IntegerField(default=0)
    address = models.CharField(max_length=100, null=True)
    city = models.ForeignKey(City, verbose_name='所在城市')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name='所属机构')
    name = models.CharField(max_length=50)
    work_years = models.SmallIntegerField(default=0, verbose_name='工作经验')
    bookmark_num = models.IntegerField(verbose_name='收藏人数')
    click_num = models.IntegerField(default=0)
    style = models.CharField(max_length=50, verbose_name='教学风格')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name
