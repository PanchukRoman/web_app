from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# функция регистрации
def Registr(request):
    data = {} # для сохранения переданных данных
    if request.method == 'POST':
        # создаем форму для записи
        form = UserCreationForm(request.POST)
        # проверка формы на правильность
        if form.is_valid():
            # сохраняем пользователя
            form.save()
            # передача форму на рендер
            data['form'] = form
            # если все ок - выводим страницу
            data['res'] = "Все прошло успешно"
            # рендеринг страницы
            return render(request, "registr.html", data)
    else:
        form = UserCreationForm()
        data['form'] = form
        return render(request, "registr.html", data)

def SignIn(request):
    pass