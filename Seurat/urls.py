from django.conf.urls import url, include

#  now we are using default router for viewset
from rest_framework.routers import DefaultRouter

from . import views

# make an instance of default router
router = DefaultRouter()

# register our HelloViewSet
router.register('try', views.TryViewset, base_name='try')


# here you will have to map your router
urlpatterns = [
    url(r'', include(router.urls)),
]