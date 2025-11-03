from django.shortcuts import render, redirect, get_object_or_404
from .models import*
from .forms import*

def teacher_base(request):
    return render(request, 'teacher/teacherbase.html')

def teacher_course(request):
    return render(request, 'teacher/teacherinsertcourse.html')