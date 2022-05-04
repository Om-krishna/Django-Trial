from django.conf.urls import url, include
from django.contrib import admin
from akirachix import views
from rest_framework import routers
from akirachix.views import greetingsViewSet

router = routers.DefaultRouter()
router.register(r'greetings', greetingsViewSet)
urlpatterns = [
    url(r'^admin/', admin.site,urls),
    url(r'^api/', include(router.urls)),
    url(r'^$', views.hii),
    url(r'^$', views.hello),
]