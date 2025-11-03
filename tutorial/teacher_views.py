from django.shortcuts import render, redirect, get_object_or_404
from .models import*
from .forms import CourseForm, TopicForm, ContentForm
from django.contrib.auth.decorators import login_required

@login_required
def teacher_base(request):
    return render(request, 'teacher/teacherbase.html')

# Teacher Course Logic Here
@login_required
def teacher_course(request):
    form = CourseForm(request.POST or None , request.FILES)
    if request.method == 'POST':
        
        if form.is_valid():
            course = form.save(commit=False)
            course.user = request.user
            course.save()
            return redirect(teacher_course)
    return render(request, 'teacher/teacherinsertcourse.html', {'form':form})

@login_required
def teacher_manageCourse(request):
    courses = Course.objects.filter(user=request.user)
    return render(request, 'teacher/teachermanageCourse.html',{'courses':courses})

@login_required
def delete_teacherCourse(request, id):
    item = Course.objects.get(id=id)
    item.delete()
    return redirect(teacher_manageCourse)

@login_required
def edit_teacherCourse(request, id):
    course = get_object_or_404(Course, id=id)
    form = CourseForm(instance=course)
    if request.method == 'POST':
        form = CourseForm(request.POST or None , instance=course)
        if form.is_valid():
            form.save()
            return redirect(teacher_manageCourse)

    return render(request, 'teacher/editteachercourse.html', {'form':form})

# Teacher Topic Logic Here 
def inserTeacherTopic(request):
    form = TopicForm(request.POST or None, user= request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(inserTeacherTopic)
    return render(request, 'teacher/teacherInsertTopic.html',{'form':form})

def manageTeacherTopic(request):
    topics = Topic.objects.select_related('course').filter(course__user=request.user)
    return render(request, 'teacher/manageTeacherTopic.html', {'topics':topics})

def deleteTeacherTopic(request, id):
    d = Topic.objects.get(id=id)
    d.delete()
    return redirect(manageTeacherTopic)

def editTeacherTopic(request, id):

    topic = get_object_or_404(Topic, id=id)
    form = TopicForm(instance = topic)
    if request.method == 'POST':
        form = TopicForm(request.POST or None, instance = topic)
        if form.is_valid():
            form.save()
            return redirect(manageTeacherTopic)
    return render(request, 'teacher/editTeacherTopic.html', {'form':form})


def insertTeacherPost(request):
    form = ContentForm(request.POST or None , user=request.user)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect(insertTeacherPost)
    return render(request, 'teacher/insertTeacherPost.html', {'form':form})
