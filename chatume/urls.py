from django.conf.urls import url
from django.contrib import admin
from chat.views import ChatterBotAppView, chatterbot_api


urlpatterns = [
    url(r'^$', ChatterBotAppView.as_view(), name='main'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^api/chatterbot/', chatterbot_api, name='chatume'),
]