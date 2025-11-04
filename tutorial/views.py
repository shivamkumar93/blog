from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
# Create your views here.


def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('after_login')
        else:
            messages.error(request, 'Invalid username or password!')
    return render(request, 'registration/login.html')


@login_required
def after_login(request):
    user = request.user
    # if user.is_superuser:
    #     return redirect('/admin/')
    # elif user.role == 'admin':
    #     return redirect('admin')     
    if user.role == 'teacher':
        return redirect('teacherbase')
    else:
        return redirect('homepage')

def home(request):
    data = {}
    data['courses'] = Course.objects.all()
    return render(request, 'public/home.html', data)

def course(request, slug, id):
    data = {}
    courses = Course.objects.get(id=id)
    topics = courses.topics.all()
    return render(request, 'public/course.html', {"topics":topics, "courses":courses})

def content(request, course_slug, course_id, topic_slug, topic_id):
    course = Course.objects.get(id=course_id)
    topics = Topic.objects.filter(course=course_id)
    contents = Content.objects.filter(topic=topic_id,status="published")
    
    return render(request, 'public/content.html', { "courses":course, "topics":topics, "contents" :contents})

def allCourses(request):
    courses = Course.objects.all()
    return render(request, 'public/allcourse.html', {"courses":courses})


def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        form.is_valid()
        form.save()
        return redirect('login')
    return render(request, "registration/register.html", {"form":form})



def search(request):
    query = request.GET.get('q') 
    results = {}

    if query:
        topics = Topic.objects.filter(Q(topic_name__icontains=query) | Q(course__name__icontains=query) )
        courses = Course.objects.filter(Q(name__icontains=query) | Q(topics__topic_name__icontains=query)
).distinct()
        # contents = Content.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))

        results = {
            'courses': courses,
            'topics': topics,
            # 'contents': contents,
        }

    return render(request, 'public/search.html', {'query': query, 'results': results})

