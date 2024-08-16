from django.shortcuts import render

from lib.payments.braintree import token


def vip(req):
    return render(req, "payments/vip.html")


def new(req):
    return render(req, "payments/new.html", {"token": token()})
