from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name='start-page'),
    path('carList/', views.home, name='carList-page'),
]
