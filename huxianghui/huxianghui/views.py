import os
from PIL import Image
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from huxianghui.settings.server import MEDIA_ROOT
from django.shortcuts import render

@require_GET
def get_asstes(request,file_path):
    path = os.path.join(MEDIA_ROOT, file_path)
    img = Image.open(path)
    response = HttpResponse(content_type='image/jpeg')
    img.convert('RGB').save(response, 'jpeg')
    return response


def get_index(request):
    return render(request, 'build/moc/index.html')