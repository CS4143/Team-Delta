from . import views
from django.urls import path

app_name = 'instructor'

urlpatterns = [
    path('', views.TestView.as_view(), name='instructor'), 
]