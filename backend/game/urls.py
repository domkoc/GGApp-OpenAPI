from django.urls import path

from . import views


urlpatterns =[
    path('lobby/new', views.create_lobby),
    path('lobby/<str:lobby_id>/start', views.start_lobby),
    path('lobby/join', views.join_lobby),
    path('game/<str:id>/round', views.round),
    path('game/<str:id>', views.game),
    path('scoreboard', views.scoreboard)

]