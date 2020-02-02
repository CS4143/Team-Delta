from . import views
from django.urls import path

app_name = 'student'

urlpatterns = [
    path('', views.TestView.as_view(), name='student'),
]