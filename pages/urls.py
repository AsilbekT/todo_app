from django.urls import path
from app.views import todo, register_user, login_user
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('todo/', todo, name='todo'),
    path('accounts/register/', register_user, name='register'),
    path('accounts/login/', login_user, name='login'),
]
