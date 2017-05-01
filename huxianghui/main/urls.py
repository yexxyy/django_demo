
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
    url(r'^user_info/$',views.get_user_info),
    url(r'^set_user_info/$',views.set_user_info),

    url(r'^get_banners/$',views.get_banners),
    url(r'^get_news/$',views.get_news),

    url(r'^bulidings/(?P<page>\d+)/$', views.get_buildings),
    url(r'^buildings_condition/(?P<page>\d+)/$',views.get_buildings_condition),
    url(r'^search_building\/?$',views.search_building),

    url(r'^get_activitys/(?P<page>\d+)/$',views.get_activitys),
    url(r'^get_collect_items/(?P<activity_id>\d+)/$',views.get_collect_items),
    url(r'^post_participator_info/$',views.save_paticipator_info),

    url(r'^set_liked/(?P<building_id>\d+)/$',views.set_liked),
    url(r'^get_user_likes/$',views.get_user_likes),

]