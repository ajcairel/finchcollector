from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('squishes/', views.squishes_index, name='index'),
    path('squishes/<int:squish_id>/', views.squishes_detail, name='detail'),
    path('squishes/create/', views.SquishCreate.as_view(), name='squish_create'),
    path('squishes/<int:pk>/update/', views.SquishUpdate.as_view(), name='squish_update'),
    path('squishes/<int:pk>/delete/', views.SquishDelete.as_view(), name='squish_delete'),
]