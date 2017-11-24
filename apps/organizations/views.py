from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, \
    PageNotAnInteger

from .models import City, CourseOrg
from .forms import UserAskForm
from courses.models import Course
from operation.models import UserFavorite

# Create your views here.


class OrgList(View):
    def get(self, request):
        page_type = 'org'
        citys = City.objects.all()
        course_orgs = CourseOrg.objects.all()
        hot_orgs = course_orgs.order_by('-click_num')[:3]
        city_id = request.GET.get('city', '')
        sort = request.GET.get('sort', '')

        if city_id:
            course_orgs = course_orgs.filter(city_id=int(city_id))

        orgs_num = course_orgs.count()

        if sort == 'stu_num':
            course_orgs = course_orgs.order_by('-student_num')

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(course_orgs, 5, request=request)
        orgs = p.page(page)

        return render(request, 'organizations/org-list.html',
                      {
                          'citys': citys,
                          'orgs': orgs,
                          'orgs_num': orgs_num,
                          'city_id': city_id,
                          'hot_orgs': hot_orgs,
                          'sort': sort,
                          'page_type': page_type,
                      })

class AddUserAsk(View):
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            userask_form.save(commit=True)
            return HttpResponse('{"status":"success"}',
                                content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"添加出错"}',
                                content_type='application/json')

class OrgCourses(View):
    def get(self, request, org_id):
        page_type = 'course'
        org_id = org_id
        org = CourseOrg.objects.get(id=int(org_id))

        # 判断机构是否已收藏
        is_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user,
                                                fav_type=2,
                                                fav_id=org.id):
                is_fav = True

        courses = org.course_set.all()
        return render(request, 'organizations/org-detail-course.html',
                      {'courses': courses,
                       'org': org,
                       'page_type': page_type,
                       'is_fav': is_fav})

class OrgTeachers(View):
    def get(self, request, org_id):
        page_type = 'teacher'
        org_id = org_id
        org = CourseOrg.objects.get(id=int(org_id))

        # 判断机构是否已收藏
        is_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user,
                                                fav_type=2,
                                                fav_id=org.id):
                is_fav = True

        teachers = org.teacher_set.all()
        return render(request, 'organizations/org-detail-teachers.html',
                      {'teachers': teachers,
                       'org': org,
                       'page_type': page_type,
                       'is_fav': is_fav})

class OrgDesc(View):
    def get(self, request, org_id):
        page_type = 'desc'
        org_id = org_id
        org = CourseOrg.objects.get(id=int(org_id))

        # 判断机构是否已收藏
        is_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user,
                                                fav_type=2,
                                                fav_id=org.id):
                is_fav = True

        description = org.description
        return render(request, 'organizations/org-detail-desc.html',
                      {'description': description,
                       'org': org,
                       'page_type': page_type,
                       'is_fav': is_fav})

class AddOrgFav(View):
    def post(self, request):
        fav_id = int(request.POST.get('fav_id', '0'))
        fav_type = int(request.POST.get('fav_type', '0'))
        user = request.user
        # 如果用户未登录，返回相应的msg，让前端跳转到登录页面
        if not user.is_authenticated():
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}',
                                content_type='application/json')
        existed_fav = UserFavorite.objects.filter(user=user,
                                                  fav_id=fav_id,
                                                  fav_type=fav_type)
        # 如果用户已收藏该机构，则取消收藏，否则添加收藏
        if existed_fav:
            existed_fav.delete()
            return HttpResponse('{"status":"success", "msg":"收藏"}',
                                content_type='application/json')
        else:
            user_fav = UserFavorite()
            user_fav.user = user
            user_fav.fav_id = fav_id
            user_fav.fav_type = fav_type
            user_fav.save()
            return HttpResponse('{"status":"success", "msg":"已收藏"}',
                                content_type='application/json')
