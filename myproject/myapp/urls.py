from django.urls import path
from . import views
from .views import osoba_list, osoba_details, person_list, person_detail, stanowisko_list, stanowisko_details, LogoutView, TeamDetail

urlpatterns = [
    path('osoby/', views.osoba_list),
    path('osoby/<int:pk>/', views.osoba_details),
    path('persons/', views.person_list),
    path('persons/<int:pk>/', views.person_detail),
    path('persons/update/<int:pk>/', views.person_update),
    path('persons/delete/<int:pk>/', views.person_delete),
    path('stanowiska/', views.stanowisko_list),
    path('stanowiska/<int:pk>/', views.stanowisko_details),
    path('welcome/', views.welcome_view),
    path('persons_html/', views.person_list_html),
    path('person_html/<int:id>', views.person_detail_html),
    path('stanowisko/<int:pk>/members', views.StanowiskoMemberView.as_view),
    path('api/logout/', views.LogoutView.as_view(), name='api_logout'),
    path('team/<int:pk>/', views.TeamDetail.as_view, name = 'team_detail')
]