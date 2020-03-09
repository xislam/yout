from django.contrib import messages
from django.shortcuts import render
from webapp.task import get_mp3
from webapp.forms import ConvertForm


def download(request):
    if request.method == 'POST':
        form = ConvertForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data.get('link')
            email = form.cleaned_data.get('email')
            url = request.get_host()
            get_mp3.delay(url, email, link)
            messages.success(request, 'Ссылка на скачивание отправлена на почту!')


    else:
        form = ConvertForm()

    return render(request, 'index.html', locals())

