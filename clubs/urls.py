from django.urls import path
from . import views  

urlpatterns = [
    path('', views.club_list, name='club-list'),
    path('club/<int:pk>/', views.club_detail, name='club-detail'),
]