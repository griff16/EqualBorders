from django.http import HttpResponse
from django.views.generic import TemplateView

class summaryDashboardView(TemplateView):
    template_name = "summaryDashboard.html"