from django.contrib import admin
from . import models

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 
                    'email', 
                    'is_student', 
                    'is_active', 
                    'is_staff', 
                    'is_superuser')

admin.site.register(models.User, UserAdmin)