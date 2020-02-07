from django.contrib import admin
from . import models

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 
                    'email', 
                    'date_joined',
                    'is_student', 
                    'is_active', 
                    'is_staff', 
                    'is_superuser']

    search_fields = ['username']

    list_filter = ['is_student', 
                   'is_active', 
                   'is_superuser',
                   'date_joined']

    fieldsets = (
        (None, {
            'fields': ('username', 'email',)
        }),
        ('Account Status', {
            'fields': ('is_active', 'is_staff', 'is_superuser', )
        })
    )

admin.site.register(models.User, UserAdmin)