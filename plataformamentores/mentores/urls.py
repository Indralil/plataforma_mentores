from django.urls import path, re_path
from .views import MentorView, FileUploadView


urlpatterns = [
    path('', MentorView.as_view()),
    re_path(r'^upload/(?P<filename>[^/]+)$', FileUploadView.as_view()),
]



