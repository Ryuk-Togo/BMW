from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = "sgf"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # path('input/', views.input, name='input'),
    # path('modify/<str:id>', views.modify, name='modify'),
    # path('delete/<str:id>', views.delete, name='delete'),
]