from . import views
from django.urls import path

app_name = 'instructor'

urlpatterns = [
    path('', views.create_course, name='instructor'), 
    path('detail/', views.course_detail, name='course_detail'),
    path('editHw/', views.edit_homework, name='edit_homework')
]