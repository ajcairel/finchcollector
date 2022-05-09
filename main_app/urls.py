from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('squishes/', views.squishes_index, name='index'),
    path('squishes/<int:squish_id>/', views.squishes_detail, name='detail'),
]