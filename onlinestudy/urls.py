
from django.contrib import admin
from django.urls import path, include
from tutorial.views import *
from tutorial.admin_views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
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
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

