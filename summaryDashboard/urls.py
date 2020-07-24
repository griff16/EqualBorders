from django.urls import path
from summaryDashboard.views import *

urlpatterns = [
    path('', summaryDashboardView.as_view(), name='sumDash'),
    path('about/', summaryDashboardAboutView.as_view(), name='sumDashAbout'),
    path('schools/', summaryDashboardSchoolsView.as_view(), name='sumDashSchools'),
    path('news/', summaryDashboardNewsView.as_view(), name='sumDashNews'),
]