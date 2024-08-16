from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from lib.payments.braintree import token


def vip(req):
    return render(req, "payments/vip.html")


@login_required
def new(req):
    return render(req, "payments/new.html", {"token": token()})
