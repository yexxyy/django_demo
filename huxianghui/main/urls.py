
from django.conf.urls import url
from . import views



urlpatterns=[

    url(r'^signup/$',views.signup),
    url(r'^signin/$',views.signin),
    url(r'^signout/$',views.signout),
    url(r'^forget/$' ,views.forget_passwd),
    url(r'^passwd_page\/?',views.passwd_page),
    url(r'^reset_passwd/$',views.reset_passwd),
    url(r'^change_passwd/$',views.change_passwd),

    url(r'^get_banners/$',views.get_banners),
    url(r'^get_news/$',views.get_news),

    url(r'^bulidings/(?P<page>\d+)/$', views.get_buildings),
    url(r'^buildings_condition/$',views.get_buildings_condition),

    url(r'^get_activitys/$',views.get_activitys),
    url(r'^get_collect_items/(?P<activity_id>\d+)/$',views.get_collect_items),
    url(r'^post_participator_info/$',views.save_paticipator_info),

]