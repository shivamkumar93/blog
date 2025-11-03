from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class User(AbstractUser):
    ROLE_CHOICES = (
        
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

class Course(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="media/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Topic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True, related_name='topics')
    slug = models.SlugField(blank=True, null=True)
    
    topic_name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.topic_name
    
class Content(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True, related_name='contents')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True, blank=True, related_name='contents')
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title    