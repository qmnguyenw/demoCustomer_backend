from django.conf.urls import url 
from django.urls import path, include
from rest_framework import routers
from users.views import * 

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [ 
    path('', include(router.urls)),
]