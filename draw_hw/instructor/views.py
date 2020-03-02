from django.shortcuts import render
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views import generic
from courses.forms import CourseForm
from courses.models import Course
from . import mixins
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.decorators import login_required

@login_required()
def create_course(request):
    # deny access for certain users
    if request.user.is_student or \
        request.user.is_superuser:
            return HttpResponseForbidden()

    c_form = CourseForm()
    courses = Course.objects.filter(instructor=request.user)
    if request.method == 'POST':
        c_form = CourseForm(request.POST)
        if c_form.is_valid():
            c_form.save()
            return HttpResponseRedirect(reverse_lazy('instructor:instructor'))
    return render(request, 'instructor/home.html', {'c_form': c_form, 
                                                    'courses': courses})
@login_required()
def course_detail(request, pk):
    # deny access for certain users
    if request.user.is_student or \
        request.user.is_superuser:
            return HttpResponseForbidden()

    courses = Course.objects.filter(instructor=request.user)
    courses = courses.filter(pk=pk)
    if request.method == 'POST':
        c_form = CourseForm(request.POST)
        if c_form.is_valid():
            c_form.save()
            return HttpResponseRedirect(reverse_lazy('instructor:instructor'))
    return render(request, 'instructor/class.html', {'courses': courses})