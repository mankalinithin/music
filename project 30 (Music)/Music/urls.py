from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('Admin',views.admin_login_view,name='Admin'),
    path('Register',views.Register_view,name='register'),
    path('dashboard',views.user_dash,name='userdashboard'),
    path('add-music',views.add_music,name='addmusic'),
    path('search-list',views.search_music,name='search'),
    path('song/<int:pk>/',views.add_playlist,name='addtoplaylist'),
    path('remove-from-playlist/<int:pk>/',views.remove_play,name='removefromplaylist')
]