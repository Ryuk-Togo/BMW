from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = "estimate"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('input/', views.input, name='input'),
    # path('estimate/<str:serial>', views.estimate, name='estimate'),
    # path('order/<str:serial>', views.order, name='order'),
    # path('delivary/<str:serial>', views.order, name='delivary'),
    # path('inspection/<str:serial>', views.order, name='inspection'),
    # path('history/<str:serial>', views.order, name='history'),
]