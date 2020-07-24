from django.http import HttpResponse
from django.views.generic import TemplateView


class summaryDashboardView(TemplateView):
    template_name = "summaryDashboard.html"


class summaryDashboardAboutView(TemplateView):
    template_name = "about.html"


class summaryDashboardSchoolsView(TemplateView):
    template_name = "schools.html"


class summaryDashboardNewsView(TemplateView):
    template_name = "news.html"
