from django.urls import path
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', authViews.LoginView.as_view(template_name='carList/loginPage.html'), name='start-page'),
    path('carList/carList.html', views.home, name='carList-page'),
]
