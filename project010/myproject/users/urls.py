from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('sign_up/', views.sign_up, name='register'),
    path('sign_in/', views.sign_in, name='login'),
    # path('sign_out/', views.sign_out, name='logout'),
    # path('profile/', views.profile, name='profile'),
    # path('profile/<int:user_id>/', views.profile, name='profile'),
    # path('profile/edit/', views.edit_profile, name='edit_profile'),
    # path('profile/edit/password/', views.change_password, name='change_password'),
    # path('profile/edit/avatar/', views.change_avatar, name='change_avatar'),
    # path('profile/edit/avatar/<int:avatar_id>/', views.change_avatar, name='change_avatar'),
    # path('profile/edit/avatar/delete/<int:avatar_id>/', views.delete_avatar, name='delete_avatar'),
    # path('profile/edit/avatar/delete/', views.delete_avatar, name='delete_avatar'),
    # path('profile/edit/avatar/delete/<int:avatar_id>/', views.delete_avatar, name='delete_avatar'),
    # path('profile/edit/avatar/delete/', views.delete_avatar, name='delete_avatar'),
    # path('profile/edit/avatar/delete/<int:avatar_id>/', views.delete_avatar, name='delete_avatar'),
    # path('profile/edit/avatar/delete/', views.delete_avatar, name='delete_avatar'),
    # path('profile/edit/avatar/delete/<int:avatar_id>/', views.delete_avatar, name='delete_avatar'),
    # path('profile/edit/avatar/delete/', views.delete_avatar, name='delete_avatar'),
]