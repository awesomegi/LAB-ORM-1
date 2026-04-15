from django.urls import path
from . import views

app_name = 'lab_blogger'

urlpatterns = [
    path('', views.home, name='home'),          # Homepage
    path('add/', views.add_post, name='add_post'),  # Add new post
]