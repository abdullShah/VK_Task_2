from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('ask/', views.ask, name='ask'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('questions/', views.questions, name='questions'),
]
