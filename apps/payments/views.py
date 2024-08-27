from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from lib.auth.group import join_group
from lib.payments.braintree import gateway, token


def vip(req):
    return render(req, "payments/vip.html")


def index(req):
    if req.method == "POST":
        nonce = req.POST["nonce"]

        result = gateway().transaction.sale(
            {
                "amount": 10,
                "payment_method_nonce": nonce,
            }
        )

        if result.is_success:
            join_group(req.user, "VIP")
            messages.success(req, "交易成功!")
        else:
            messages.error(req, "交易失敗!")

        return redirect("/")


@login_required
def new(req):
    return render(req, "payments/new.html", {"token": token()})
