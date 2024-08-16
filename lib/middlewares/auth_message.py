from django.contrib import messages

from core.settings import LOGIN_URL


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, req):
        resp = self.get_response(req)
        if resp.status_code == 302 and resp.url.startswith(str(LOGIN_URL)):
            messages.warning(req, "請先登入會員帳號")

        return resp
