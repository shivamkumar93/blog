from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    role = forms.ChoiceField(choices=User.ROLE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password1', 'password2']

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