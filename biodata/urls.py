from django.contrib import admin
from django.urls import path
from pribadiapp.views import pribadi, tambahkan

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pribadi, name="home"),
    path('tambahkan/', tambahkan, name="tambahkan"),
]
