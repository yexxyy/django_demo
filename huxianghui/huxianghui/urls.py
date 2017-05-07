"""huxianghui URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main/',include('main.urls')),
    url(r'^assets/(?P<file_path>.*)',views.get_asstes),

    url(r'^index.html',views.index),
    url(r'^list.html',views.list),
    url(r'^reg_login.html',views.reg_login),
    url(r'^form.html',views.form),
    url(r'^person.html',views.person),
    url(r'^reg_change.html',views.reg_change),
    url(r'^reg_forget.html',views.reg_forget),
    url(r'^reg_info.html',views.reg_info),
    url(r'^reg_login.html',views.reg_login),
    url(r'^reg_register.html',views.reg_register),
    url(r'^search.html',views.search),
    url(r'^select.html',views.select),
    url(r'select_input.html^',views.select_input),
    url(r'^select_score.html',views.select_score),
    url(r'^test-detail.html', views.test_detail),
    # url(r'^', views.),
    # url(r'^', views.),
    # url(r'^', views.),
    # url(r'^', views.),
    # url(r'^', views.),
    #
]
