from django.contrib import admin
from django.urls import re_path,include
from .import views


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', views.firstpage, name='firstpage'),
    re_path(r'app/', include('app.urls')),

]