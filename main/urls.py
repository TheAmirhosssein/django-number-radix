from django.urls import path

from main.views import HomePage

urlpatterns = [path("", HomePage.as_view(), name="home-page")]
