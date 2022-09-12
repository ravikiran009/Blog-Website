from django.urls import path
from .views import UserRegisterView,UserEditView,PasswordChangeView,ShowProfileView,EditProfilePageView,CreateProfileView

urlpatterns=[

    path('signup/',UserRegisterView.as_view(),name='signup'),
    path('edit_profile/',UserEditView.as_view(),name='edit-profile'),
    path('password/',PasswordChangeView.as_view(),name='password'),
    path('<int:pk>/profile/',ShowProfileView.as_view(),name='user-profile'),
    path('<int:pk>/edit_profile_page/',EditProfilePageView.as_view(),name='edit-profile-page'),
    path('create_profile_page/',CreateProfileView.as_view(),name='create-profile-page'),
]