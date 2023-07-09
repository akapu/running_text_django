from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.utils import timezone
from .running_text import create_video
from .models import Query
import os


def index(request):
    return HttpResponse("it-solution.ru")

def video(request):
    TEXT = request.GET.get("text", "")

    q = Query(text=TEXT, date=timezone.now())
    q.save()

    FILENAME = f"video{q.id}.mp4"

    create_video(settings.FONTNAME, TEXT, FILENAME)

    with open(FILENAME, "rb") as f:
        file_data = f.read()

    os.remove(FILENAME)

    response = HttpResponse(file_data, content_type="video/mp4")
    response["Content-Disposition"] = "attachment; filename=video.mp4"

    return response
