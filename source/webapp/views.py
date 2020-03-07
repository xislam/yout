import youtube_dl
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib import messages

from main import settings
from main.celery import app
from .forms import ConvertForm


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


@app.task
def get_mp3(url, email, link):
    DOWNLOAD_OPTIONS_MP3 = {

        'format': 'bestaudio/best',
        'outtmpl': 'audio/%(title)s.%(ext)s',
        'nocheckcertificate': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(DOWNLOAD_OPTIONS_MP3) as dl:
        result = dl.extract_info(link)
        filename = result['title'].replace(' ', '%20').replace(' - ', '%20').replace(' | ', '%20')

    download_link = 'http://' + url + '/media/' + filename.replace(' ', '%20').replace(' - ', '%20').replace(' | ',
                                                                                                             '%20') + '.mp3'
    send_mail('Ссылка на скачивание файла', download_link, settings.EMAIL_HOST_USER, [email], fail_silently=False, )
