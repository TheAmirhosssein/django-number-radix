from django.urls import path

from main.views import DecryptView, HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home-page"),
    path("decrypt/", DecryptView.as_view(), name="decrypt-page"),
]
