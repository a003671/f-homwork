from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    object_list = Student.objects.order_by('group')
    teachers_list = Teacher.objects.all()
    context = {
        'object_list': object_list,
        'teachers_list': teachers_list,
        }

    return render(request, template, context)