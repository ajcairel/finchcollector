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
    path('squishes/<int:squish_id>/add_size/', views.add_size, name='add_size'),

    path('squishes/<int:squish_id>/assoc_squad/<int:squad_id>/', views.assoc_squad, name='assoc_squad'),
    path('squishes/<int:squish_id>/unassoc_squad/<int:squad_id>/', views.unassoc_squad, name='unassoc_squad'),
    path('squads/', views.SquadList.as_view(), name='squads_index'),
    path('squads/<int:pk>/', views.SquadDetail.as_view(), name='squads_detail'),
    path('squads/create/', views.SquadCreate.as_view(), name='squads_create'),
    path('squads/<int:pk>/update/', views.SquadUpdate.as_view(), name='squads_update'),
    path('squads/<int:pk>/delete/', views.SquadDelete.as_view(), name='squads_delete'),
]