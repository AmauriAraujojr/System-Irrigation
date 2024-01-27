from django.urls import path
from .views import ServiceView, ServicesDetailView

urlpatterns=[
    path("services/",ServiceView.as_view()),
    path("services/<int:pk>/",ServicesDetailView.as_view())
]
