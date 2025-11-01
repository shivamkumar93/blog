from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import user_passes_test

# ye decorator sirf superuser ko allow karega
admin_required = user_passes_test(lambda u: u.is_superuser, login_url='/')


@admin_required
def adminpage(request):
    return render(request, 'admin/adminbase.html')

@admin_required
def insertCourse(request):
    
    form = CourseForm(request.POST or None, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(insertCourse)

    return render(request, 'admin/insertCourse.html', {'form':form})

@admin_required
def editCourse(request, id):
    course = get_object_or_404(Course, id=id)
    form = CourseForm(instance=course)
    if request.method == 'POST':
        form = CourseForm(request.POST or None , instance=course)
        if form.is_valid():
            form.save()
            return redirect(manageCourse)
    return render(request, 'admin/editcourse.html', {"form":form})


@admin_required
def deleteCourse(request, id):
    item = Course.objects.get(id=id)
    item.delete()
    return redirect(manageCourse)


@admin_required
def insertTopic(request):
    form = TopicForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(insertTopic)
    return render(request, 'admin/insertTopic.html', {"form":form})

@admin_required
def editTopic(request, id):
    topic = get_object_or_404(Topic, id=id )
    form = TopicForm(instance=topic)
    if request.method == 'POST':
        form = TopicForm(request.POST or None , instance=topic)
        if form.is_valid():
            form.save()
            return redirect(manageTopic)
        
    return render(request, "admin/edittopic.html", {"form":form})

@admin_required
def deleteTopic(request, id):
    item = Topic.objects.get(id=id)
    item.delete()
    return redirect(manageTopic)


@admin_required
def insertContent(request):
    form = ContentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(insertContent)
    return render(request, 'admin/insertContent.html',{"form":form})

@admin_required
def editContent(request, id):
    post = get_object_or_404(Content, id=id)
    form = ContentForm(instance=post)
    if request.method == 'POST':
        form = ContentForm(request.POST or None, instance=post)
        if form.is_valid():
            form.save()
            return redirect(managePost)
    return render(request, 'admin/editcontent.html', {"form":form})

@admin_required
def deleteContent(request, id):
    item = Content.objects.get(id=id)
    item.delete()
    return redirect(managePost)

@admin_required
def manageCourse(request):
    courses = Course.objects.all()
    return render(request , "admin/managecourse.html", {"courses":courses})

@admin_required
def manageTopic(request):
    topics = Topic.objects.select_related('course').all()
    return render(request, "admin/managetopic.html", {"topics":topics})

@admin_required
def managePost(request):
    posts = Content.objects.select_related('course').select_related('topic').all()

    return render(request, "admin/managepost.html", {'posts':posts})

@admin_required
def postPublished(request, id):
    post = get_object_or_404(Content, id=id)
    
    if post.status == 'published':
        post.status = 'draft'
    else:
        post.status = 'published'
    post.save()
    return redirect(managePost)