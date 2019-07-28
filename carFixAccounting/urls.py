from django.contrib import admin
from django.urls import path, include
from users import views as userViews
from django.contrib.auth import views as authViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/',userViews.register, name='reg'),
    path('profile/',userViews.profile, name='profile'),
    path('', include('carList.urls')),
    path('exitPage', authViews.LogoutView.as_view(template_name='carList/exitPage.html'), name='exit'),

]
