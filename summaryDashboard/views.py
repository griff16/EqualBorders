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
    model = Post
    context_object_name = 'newsFeeds'

# this is News page
class summaryDashboardNewsView(ListView):
    template_name = "news.html"
    model = Post
    context_object_name = 'newsFeeds'


# one parameter named request
def colleges_upload(request):
    # declaring template
    template = "Colleges_upload.html"
    data = College.objects.all()

    # prompt is a context variable that can have different values depending on their context
    prompt = {
        'order': 'code, name, link',
        'profiles': data
    }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']

    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')


    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = College.objects.update_or_create(
            code=column[0],
            name=column[1],
            link=column[2],
        )
    context = {}
    return render(request, template, context)
