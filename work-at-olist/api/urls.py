from django.conf.urls import include, url
from django.http import HttpResponse
from rest_framework import routers

from api.views import ChannelsView

router = routers.DefaultRouter()
router.register(r'channels', ChannelsView)

urlpatterns = [
    url(r'^', include(router.urls)),
]
