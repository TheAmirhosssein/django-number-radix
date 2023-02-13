from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from components.algorithm import encrypt


class HomePageView(TemplateView):
    template_name = "main/home.html"


class DecryptView(TemplateView):
    template_name = "main/decrypt.html"


class EncryptView(TemplateView):
    template_name = "main/encrypt.html"


def encrypt_operation(request: HttpRequest):
    number = int(request.GET.get("number"))
    radix = int(request.GET.get("radix"))
    final_number = encrypt(number, radix)
    if radix > 20:
        final_number = "your radix must be lower than 21"
    return render(
        request,
        template_name="main/includes/encrypt_result.html",
        context={"result": final_number},
    )
