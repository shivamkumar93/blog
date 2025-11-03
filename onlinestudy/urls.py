
from django.contrib import admin
from django.urls import path, include
from tutorial.views import *
from tutorial.admin_views import *
from tutorial.teacher_views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', custom_login, name='login'),
    path('accounts/after-login/', after_login, name='after_login'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("account/register/", register, name ="registerpage"),
    path("", home, name="homepage"),
    path("allcourse/", allCourses, name="allcourse"),

    path("course/<str:slug>/<int:id>/", course, name="coursedetails"),
    path("content/<str:course_slug>/<int:course_id>/<str:topic_slug>/<int:topic_id>/", content, name="contentdetails"),
    path('search/', search, name='search'),


    # admin urls
    path('adminbase/',adminpage, name="admin" ),
    path('insert-course/',insertCourse, name="insertCourse" ),
    path('delete-course/<int:id>',deleteCourse, name="deletecourse" ),
    path('edit-course/<int:id>/',editCourse, name="editcourse" ),
    path('insert-topic/',insertTopic, name="insertTopic" ),
    path('edit-topic/<int:id>/',editTopic, name="edittopic" ),
    path('delete-topic/<int:id>/',deleteTopic, name="deleteTopic" ),
    path('insert-content/',insertContent, name="insertcontent" ),
    path('edit-content/<int:id>/',editContent, name="editcontent" ),
    path('delete-content/<int:id>/',deleteContent, name="deletecontent" ),
    path('managecourse/',manageCourse, name="managecourse" ),
    path('managetopic/',manageTopic, name="managetopic" ),
    path('managepost/',managePost, name="managepost" ),
    path('publishedpost/<int:id>/',postPublished, name="publishedpost" ),


    # Teacher Urls
    path('teacher_dashboard', teacher_base, name='teacherbase'),
    #course urls here 
    path('teacher_course', teacher_course, name='teacherInserCourse'),
    path('teacher_manage_course', teacher_manageCourse, name='teacherManageCourse'),
    path('deleteCourse/<int:id>/', delete_teacherCourse, name='deleteCourse'),
    path('editCourse/<int:id>/', edit_teacherCourse, name='editCourse'),
    # topic urls here
    path('insertTopic', inserTeacherTopic, name='insertTeacherTopic'),
    path('manageTeacherTopic', manageTeacherTopic, name='manageTeacherTopic'),
    path('deleteTeacherTopic/<int:id>/', deleteTeacherTopic, name='deleteTeacherTopic'),
    path('editTeacherTopic/<int:id>/', editTeacherTopic, name='editTeacherTopic'),
    # post urls here
    path('insertTeacherPost', insertTeacherPost, name='insertTeacherPost')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

