from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = "todo"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # path('dotodo/<int:row>', views.dotodo, name='dotodo'),
    path('dotodo/', views.dotodo, name='dotodo'),
    path('daytodo/', views.daytodo, name='daytodo'),
    path('todoval/', views.todoval, name='todoval'),
]
