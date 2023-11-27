from rest_framework import routers

from django.contrib import admin
from django.urls import include, path

from todo.views import TodoViewSet, UserViewSet


router = routers.DefaultRouter()
router.register(r'todos', TodoViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
