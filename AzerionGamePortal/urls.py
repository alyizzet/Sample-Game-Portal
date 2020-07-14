from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from games import views

urlpatterns = [
    path('', views.homepage),
    path('admin/', admin.site.urls)
]

urlpatterns += staticfiles_urlpatterns()
