from django.shortcuts import render, redirect, get_object_or_404
from .models import*
from .forms import CourseForm, TopicForm, ContentForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

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
@login_required
def inserTeacherTopic(request):
    form = TopicForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(inserTeacherTopic)
    return render(request, 'teacher/teacherInsertTopic.html',{'form':form})

@login_required
def manageTeacherTopic(request):
    topics = Topic.objects.select_related('course').filter(course__user = request.user)
    return render(request, 'teacher/manageTeacherTopic.html', {'topics':topics})

@login_required
def deleteTeacherTopic(request, id):
    d = Topic.objects.get(id=id)
    d.delete()
    return redirect(manageTeacherTopic)

@login_required
def editTeacherTopic(request, id):

    topic = get_object_or_404(Topic, id=id)
    form = TopicForm(instance = topic)
    if request.method == 'POST':
        form = TopicForm(request.POST or None, instance = topic)
        if form.is_valid():
            form.save()
            return redirect(manageTeacherTopic)
    return render(request, 'teacher/editTeacherTopic.html', {'form':form})


# Teacher Post Logic Here 
@login_required
def insertTeacherPost(request):
    form = ContentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            
            return redirect(insertTeacherPost)
    return render(request, 'teacher/insertTeacherPost.html', {'form':form})

# this logic for javascripts
def load_topics(request):
    course_id = request.GET.get('course_id')
    topics = Topic.objects.filter(course_id=course_id).values('id', 'topic_name')
    return JsonResponse(list(topics), safe=False)

@login_required
def manageTeacherPost(request):
    posts = Content.objects.select_related('course').filter(author = request.user)
    return render(request, 'teacher/manageTeacherPost.html',{'posts':posts})

@login_required
def deleteTeacherPost(request, id):
    item = Content.objects.get(id=id)
    item.delete()
    return redirect(manageTeacherPost)

@login_required
def editTeacherPost(request, id):
    post = get_object_or_404(Content, id=id)
    form = ContentForm(instance=post)
    if request.method == 'POST':
        form = ContentForm(request.POST or None, instance=post)
        if form.is_valid():
            form.save()
            return redirect(manageTeacherPost)
    return render(request, 'teacher/editTeacherPost.html', {'form':form})

@login_required
def teacherPostPublished(request, id):
    post = get_object_or_404(Content, id=id)

    if post.status == 'published':
        post.status = 'draft'
    else:
        post.status = 'published'
    post.save()
    return redirect(manageTeacherPost)