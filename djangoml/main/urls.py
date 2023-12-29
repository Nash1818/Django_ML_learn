from django.urls import path
from . import views

# routing:
urlpatterns = [
    path('', views.welcome, name = 'welcome'),
    path('user', views.user, name = 'user')
]
