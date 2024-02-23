from django.urls import path
from .views import UserView,UserDetailView
from rest_framework_simplejwt import views

urlpatterns=[
    path("users/",UserView.as_view()),
    path("login/", views.TokenObtainPairView.as_view()),
    path("users/<int:pk>/", UserDetailView.as_view())
]
