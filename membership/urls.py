from django.urls import path
from .views import UserRegistrationView, UserEditView, PasswordChangeView, ProfilePageView, EditProfilePageView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit-profile'),
    path('password/', PasswordChangeView.as_view()),
    path('<int:pk>/profile/', ProfilePageView.as_view(), name='profile-page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit-profile-page'),
]