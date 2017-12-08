from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pods/', views.get_pod_list, name='get_pod_list'),
]