from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('new/<str:pk>', views.new, name='new'),
]
