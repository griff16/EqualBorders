from django.urls import path
from .views import summaryDashboardView

urlpatterns = [
    path('', summaryDashboardView, name='sumDash'),
]