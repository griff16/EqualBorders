from django.urls import path
from summaryDashboard.views import summaryDashboardView

urlpatterns = [
    path('', summaryDashboardView.as_view(), name='sumDash'),
]