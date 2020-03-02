import youtube_dl
from django.shortcuts import render
from youtube_dl import YoutubeDL
import os.path
from django.contrib import messages
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }],
}


def download(request):
    if request.method == "POST":
        url = request.POST.get('link')
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messages.success(request, 'Audio your Download directory!')
    return render(request, 'index.html')

