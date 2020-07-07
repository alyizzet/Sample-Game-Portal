from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from games import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage)
]

urlpatterns += staticfiles_urlpatterns()
