from courses.models import Course
from django import forms

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'class_name', 'instructor', 'description']