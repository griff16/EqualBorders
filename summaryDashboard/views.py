import csv, io
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.db.models import Q
from .forms import SearchForm
from .models import Post, College


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

    def get_queryset(self):
        query = 'None' if self.request.GET.get('q') is None else self.request.GET.get('q')
        query_set = College.objects.filter(Q(name__icontains=query) | Q(code__icontains=query) | Q(link__icontains=query))
        
        return query_set
    

# this is News page
class summaryDashboardNewsView(ListView):
    template_name = "news.html"
    model = Post
    context_object_name = 'newsFeeds'