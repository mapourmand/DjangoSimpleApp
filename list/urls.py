from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ls/', views.infoListView.as_view(), name='list'),
    path('add/', views.add_info_form, name='add'),

]