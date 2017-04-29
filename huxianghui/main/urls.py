
from django.conf.urls import url
from . import views



urlpatterns=[
    url(r'^signup/$',views.signup),
    url(r'signin/$',views.signin),
    url(r'signout/$',views.signout),
    url(r'forget/$' ,views.forget_passwd),
    url(r'passwd_page\/?',views.passwd_page),
    url(r'resetpasswd/$',views.reset_passwd),


]