from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login

from apps.users.forms import LoginForm


class LoginView(View):
    def get(self, request):
        return render(request, "index.html")

    def post(self, request):
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            # 用于检测用户名密码是否存在
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # 验证用户是否存在, 密码是否正确

            # 查询用户是否存在
            if user is not None:
                # 查询到用户
                login(request, user)
                # 登录后跳转
                return render(request, "index.html")
            else:
                # 未查询到用户
                return render(request, "login.html")

        else:
            return render(request, "login.html", {"msg": "用户名或密码错误"})
