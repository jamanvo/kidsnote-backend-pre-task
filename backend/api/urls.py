from django.urls import path, include

urlpatterns = [path("members/", include("api.members.urls"))]
