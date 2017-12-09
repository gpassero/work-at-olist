from django.conf.urls import include, url
from django.http import HttpResponse
from rest_framework import routers

from api.views import ChannelsView, CategoriesView

router = routers.DefaultRouter()
router.register(r'channels', ChannelsView)
router.register(r'categories', CategoriesView)

urlpatterns = [
    url(r'^', include(router.urls)),
]
