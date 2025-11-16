from django.urls import path
from . import views  

urlpatterns = [
    # Club URLs
    path('', views.club_list, name='club-list'),
    path('club/<int:pk>/', views.club_detail, name='club-detail'),
    path('club/new/', views.club_create, name='club-create'),
    path('club/<int:pk>/edit/', views.club_edit, name='club-edit'),
    path('club/<int:pk>/delete/', views.club_delete, name='club-delete'),
    
    # Project URLs
    path('club/<int:pk>/new-project/', views.project_create, name='project-create'),
    path('project/<int:pk>/', views.project_detail, name='project-detail'),
    path('project/<int:pk>/edit/', views.project_edit, name='project-edit'),
    path('club/<int:pk>/delete-project/<int:project_id>/', views.delete_project, name='delete-project'),

    
    # Event URLs
    path('event/<int:pk>/', views.event_detail, name='event-detail'),
    path('event/<int:pk>/edit/', views.event_edit, name='event-edit'),
    path('club/<int:pk>/delete-event/<int:event_id>/', views.delete_event, name='delete-event'),
    path('club/<int:pk>/add-event/', views.add_event, name='add-event'),
    
    # Membership URLs
    path('club/<int:pk>/delete-member/<int:membership_id>/', views.delete_member, name='delete-member'),
    path('club/<int:pk>/set-role/<int:membership_id>/', views.set_member_role, name='set-member-role'),
]