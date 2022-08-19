from django.urls import path
from .views import MentorView


urlpatterns = [
    path('', MentorView.as_view()),
]



