from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pods/', views.get_pod_list, name='get_pod_list'),
    path('deploy/', views.get_deploy_list, name='get_deploy_list'),
    path('namespace/', views.get_namespace_list, name='get_namespace_list'),
]