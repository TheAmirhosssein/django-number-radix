from django.urls import path

from main.views import DecryptView, EncryptView, HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home-page"),
    path("decrypt/", DecryptView.as_view(), name="decrypt-page"),
    path("encrypt/", EncryptView.as_view(), name="encrypt-page"),
]
