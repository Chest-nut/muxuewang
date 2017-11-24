from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, \
    PageNotAnInteger

from .models import City, CourseOrg
from .forms import UserAskForm
from courses.models import Course

# Create your views here.


class OrgList(View):
    def get(self, request):
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

        return render(request, 'org-list.html',
                      {
                          'citys': citys,
                          'orgs': orgs,
                          'orgs_num': orgs_num,
                          'city_id': city_id,
                          'hot_orgs': hot_orgs,
                          'sort': sort,
                      })

class AddUserAsk(View):
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            userask_form.save(commit=True)
            return HttpResponse('{"status":"success"}',
                                content_type='text/plain')
        else:
            return HttpResponse("{'status':'fail', 'msg':'添加出错'}",
                                content_type='text/plain')

class OrgCourses(View):
    def get(self, request, org_id):
        page_type = 'course'
        org_id = org_id
        org = CourseOrg.objects.get(id=int(org_id))
        courses = org.course_set.all()
        return render(request, 'org-detail-course.html',
                      {'courses': courses,
                       'org': org,
                       'page_type': page_type})

class OrgTeachers(View):
    def get(self, request, org_id):
        page_type = 'teacher'
        org_id = org_id
        org = CourseOrg.objects.get(id=int(org_id))
        teachers = org.teacher_set.all()
        return render(request, 'org-detail-teachers.html',
                      {'teachers': teachers,
                       'org': org,
                       'page_type': page_type})

class OrgDesc(View):
    def get(self, request, org_id):
        page_type = 'desc'
        org_id = org_id
        org = CourseOrg.objects.get(id=int(org_id))
        description = org.description
        return render(request, 'org-detail-desc.html',
                      {'description': description,
                       'org': org,
                       'page_type': page_type})

class AddOrgFav(View):
    def post(self, request):
        fav_id = request.POST.get('fav_id', 0)
        fav_type = request.POST.get('fav_type', 0)
