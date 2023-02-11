from django.shortcuts import render
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "main/home.html"


class DecryptView(TemplateView):
    template_name = "main/decrypt.html"
