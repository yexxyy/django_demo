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


def index(request):
    return render(request, 'build/moc/index.html')

def list(request):
    return render(request, 'build/moc/list.html')

def form(request):
    return render(request, 'build/moc/form.html')

def person(request):
    return render(request, 'build/moc/person.html')

def reg_change(request):
    return render(request, 'build/moc/reg_change.html')

def reg_forget(request):
    return render(request, 'build/moc/reg_forget.html')

def reg_info(request):
    return render(request, 'build/moc/reg_info.html')

def reg_like(request):
    return render(request, 'build/moc/reg_like.html')

def reg_login(request):
    return render(request, 'build/moc/reg_login.html')

def reg_register(request):
    return render(request, 'build/moc/reg_register.html')

def search(request):
    return render(request, 'build/moc/search.html')

def select(request):
    return render(request, 'build/moc/select.html')

def select_input(request):
    return render(request, 'build/moc/select_input.html')

def select_score(request):
    return render(request, 'build/moc/select_score.html')

def test_detail(request):
    return render(request, 'build/moc/test-detail.html')