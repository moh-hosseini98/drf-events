from django.urls import path
from .views import EventListCreateAPIView,EventDetailAPIView,RegisterEventAPIView

urlpatterns = [
    path("events/",EventListCreateAPIView.as_view()),
    path("events/<int:pk>/",EventDetailAPIView.as_view()),
    path("events/<int:id>/register/",RegisterEventAPIView.as_view())
]
