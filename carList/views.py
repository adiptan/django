from django.shortcuts import render

data = [
    {
        'title': ''
    }
]

def home(request):
    return render(request, 'carList/carList.html', {'title': 'Ваша страница'})

def loginPage(request):
    return render(request, 'carList/loginPage.html', {'title': 'Авторизация'})
