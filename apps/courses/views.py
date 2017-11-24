from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class CourseList(View):
    def get(self, request):
        page_type = 'course'
        return render(request, 'course-list.html',
                      {'page_type': page_type,})