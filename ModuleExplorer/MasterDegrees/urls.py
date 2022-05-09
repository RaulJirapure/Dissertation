from django.urls import path

from . import views

urlpatterns = [
    path('', views.module_searcher, name='module_searcher'),
    path('results/<str:search>', views.module_results, name='module_results'),
    path('modules', views.modules_list, name='modules_list'),
    path('master', views.master_list, name='master_list'),
    path('module/<int:id>', views.module, name='module'),
    path('master/<int:id>', views.master, name='master'),
    path('aboutus', views.aboutus, name='aboutus'),
]
