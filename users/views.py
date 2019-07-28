from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserOurReg

def register(request):
    if request.method == "POST":
        form = UserOurReg(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} успешно зарегистрирован.')
            return redirect('carList-page')
    else:
        form = UserOurReg()
    return render(request, 'users/registration.html', {'form': form, 'title':'Регистрация пользователя'} )
