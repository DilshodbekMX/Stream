
from django.contrib import admin
from django.urls import path
from .views import index, videoStream

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path("/<str:camera_ip>/", videoStream, name="videoStream"),

]
