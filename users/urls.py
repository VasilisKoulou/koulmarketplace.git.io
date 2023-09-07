from django.urls import path 
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),

    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.userProfile, name="user_profile"),
    path('account/', views.userAccount, name='account'),

    path('edit-account/', views.editAccount, name="edit-account"),
    path('create-category/', views.createCategory, name="create-category"),
    path('update-category/<str:pk>/', views.updateCategory, name="update-category"),
    path('delete-category/<str:pk>/', views.deleteCategory, name="delete-category"),

    path('inbox/', views.inbox, name='inbox'),
    path('message/<str:pk>/', views.viewMessage, name='message'),
    path('send-message/<str:pk>/', views.createMessage, name='send-message'),

]