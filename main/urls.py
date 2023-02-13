from django.urls import path

from main.views import (
    DecryptView,
    EncryptView,
    HomePageView,
    decrypt_operation,
    encrypt_operation,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home-page"),
    path("decrypt/", DecryptView.as_view(), name="decrypt-page"),
    path("decrypt/operation/", decrypt_operation, name="decrypt-operation"),
    path("encrypt/", EncryptView.as_view(), name="encrypt-page"),
    path("encrypt/operation/", encrypt_operation, name="encrypt-operation"),
]
