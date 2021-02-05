from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = "mailbk"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^(?P<url>\w+)/$', views.index, name='index'),
    path('<str:url>', views.index, name='index'),
    path('mail/<str:url>', views.mail, name='mail'),
    path('download/<str:url>', views.download, name='download'),
]