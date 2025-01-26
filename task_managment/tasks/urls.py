from django.contrib import admin
from django.urls import path
from tasks.views import admin_dashboard
from tasks.views import user_dashboard
from tasks.views import test

urlpatterns = [
    path('admin-dashboards',admin_dashboard),
    path('user-dashboards',user_dashboard),
    path('test',test)
]
