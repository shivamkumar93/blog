from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'role', 'is_staff', 'is_active']
    search_fields = ['username', 'email', 'role']
    fieldsets = UserAdmin.fieldsets + (
        ('Role Information', {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Role Information', {'fields': ('role',)}),
    )

admin.site.register(User, CustomUserAdmin)

admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(Content)