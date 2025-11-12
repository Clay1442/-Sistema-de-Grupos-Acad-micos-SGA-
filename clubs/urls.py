from django.urls import path
from . import views  

urlpatterns = [
    path('', views.club_list, name='club-list'),
    path('club/<int:pk>/', views.club_detail, name='club-detail'),
    path('club/new/', views.club_create, name='club-create'),
    path('club/<int:pk>/delete-member/<int:membership_id>/', views.delete_member, name='delete-member'),
    path('club/<int:pk>/add-event/', views.add_event, name='add-event'),
    path('club/<int:pk>/edit/', views.club_edit, name='club-edit'),
    path('club/<int:pk>/delete/', views.club_delete, name='club-delete'),
]