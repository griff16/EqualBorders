import csv
import io
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Post, College
from django.shortcuts import render
from django.contrib import messages

# this is home page
class summaryDashboardView(ListView):
    template_name = "summaryDashboard.html"
    model = Post
    context_object_name = 'newsFeeds'

# this is about page
class summaryDashboardAboutView(ListView):
    template_name = "about.html"
    model = Post
    context_object_name = 'newsFeeds'

# this is Schools page
class summaryDashboardSchoolsView(ListView):
    template_name = "schools.html"
    model = College
    context_object_name = 'schools'

# this is News page
class summaryDashboardNewsView(ListView):
    template_name = "news.html"
    model = Post
    context_object_name = 'newsFeeds'