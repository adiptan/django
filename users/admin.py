from django.contrib import admin
from .models import Profile

admin.site.register(Profile) # регистрируем новую таблицу в админ панеле
