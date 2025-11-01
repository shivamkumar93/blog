from django.forms import ModelForm
from .models import *

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = "__all__"

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['course', 'topic_name', 'slug', 'description']


class ContentForm(ModelForm):
    class Meta:
        model = Content
        fields = "__all__"