
from django.conf.urls import url
from . import views



urlpatterns=[

    url(r'^signup/$',views.signup),
    url(r'signin/$',views.signin),
    url(r'signout/$',views.signout),
    url(r'forget/$' ,views.forget_passwd),
    url(r'passwd_page\/?',views.passwd_page),
    url(r'reset_passwd/$',views.reset_passwd),
    url(r'change_passwd/$',views.change_passwd),

    url(r'^bulidings/(?P<page>\d+)/$', views.get_buildings),
]