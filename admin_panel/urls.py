from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views
app_name = "admin_panel"
urlpatterns = [
    path("dashboard", views.admin_homebase, name="dashboard"),
    
]