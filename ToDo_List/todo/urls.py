from django.urls import path
from . import views

app_name='todo'

urlpatterns = [
    path('', views.homepage, name='home'),
    path('delete/<int:id>/', views.Item_Delete, name='item-delete'),
    path('cross_off/<int:id>/', views.cross_off, name='item-cross-off'),
    path('uncross/<int:id>/', views.uncross, name='item-uncross'),
    path('edit/<int:id>/', views.edit_view, name='item-edit'),
]
