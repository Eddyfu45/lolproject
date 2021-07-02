# main_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('champions/', views.champions_index, name='champions_index'),
    path('champions/<int:champion_id>/', views.champions_show, name='champions_show'),
    path('champions/create/', views.ChampionCreate.as_view(), name ='champions_create'),
    path('champions/<int:pk>/update/', views.ChampionUpdate.as_view(), name='champions_update'),
    path('champions/<int:pk>/delete/', views.ChampionDelete.as_view(), name='champions_delete'),
    path('user/<username>/', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('user/<username>/', views.profile, name='profile')
]
