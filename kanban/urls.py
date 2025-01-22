from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('kanban/', views.kanban_view, name='kanban'),
    path('add/', views.add_prospect, name='add_prospect'),
    path('login/', views.custom_login_view, name='login'),
]