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
        fields = ['name','slug','description','image']

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['course', 'topic_name', 'slug', 'description']
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)   # accept the logged-in user
        super(TopicForm, self).__init__(*args, **kwargs)
        if user:
            # only show courses created by this teacher
            self.fields['course'].queryset = Course.objects.filter(user=user)


class ContentForm(ModelForm):
    class Meta:
        model = Content
        # fields = "__all__"
        exclude = ['author']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)   # accept the logged-in user
        super(ContentForm, self).__init__(*args, **kwargs)
        if user:
            # only show courses created by this teacher
            self.fields['course'].queryset = Course.objects.filter(user=user)

            self.fields['topic'].queryset = Topic.objects.filter(course__user=user)