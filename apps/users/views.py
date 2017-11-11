from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.db.utils import IntegrityError
from django.shortcuts import render
from django.views.generic.base import View

from .forms import LoginForm, RegisterForm, ForgetPasswordForm, ResetPasswordForm
from .models import UserInfo, EmailVerificationCode
from utils.sendemail import send_verification_email

# Create your views here.

class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        user = UserInfo.objects.get(Q(username=username)|Q(email=username)|Q(mobile=username))
        if user.check_password(password):
            return user


class ActiveUser(View):
    def get(self, request, active_code):
        emailvc = EmailVerificationCode.objects.get(code=active_code)
        if emailvc:
            email = emailvc.email
            user = UserInfo.objects.get(username=email)
            user.is_active = True
            user.save()

        return render(request, 'login.html', {})


class Login(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active is True:
                    login(request, user)
                    return render(request, 'index.html', {})
                else:
                    return render(request, 'login.html', {'msg': '用户未激活，请登录邮箱激活！'})
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误！'})
        else:
            return render(request, 'login.html', {'login_form': login_form})


class Register(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            user = UserInfo()
            user.is_active = False
            user.username = email
            user.email = email
            user.password = make_password(password)
            try:
                user.save()
            except IntegrityError:
                return render(request, 'register.html', {'msg': '该邮箱已注册'})
            send_verification_email(email, 'register')
            return render(request, 'login.html', {})
        else:
            return render(request, 'register.html', {'register_form': register_form})


class ForgetPassword(View):
    def get(self, request):
        forgetpw_form = ForgetPasswordForm()
        return render(request, 'forgetpwd.html', {'forgetpw_form': forgetpw_form})

    def post(self, request):
        forgetpw_form = ForgetPasswordForm(request.POST)
        if forgetpw_form.is_valid():
            email = request.POST.get('email', '')
            send_verification_email(email, 'forget')
            return render(request, 'sendemail_success.html', {})
        else:
            return render(request, 'register.html', {'register_form': forgetpw_form})


class ResetPassword(View):
    def get(self, request, reset_code):
        emailvc = EmailVerificationCode.objects.get(code=reset_code)
        if emailvc:
            email = emailvc.email
            return render(request, 'password_reset.html', {'email': email,
                                                           'reset_code': reset_code})

    def post(self, request, reset_code):
        resetpwd_form = ResetPasswordForm(request.POST)
        if resetpwd_form.is_valid():
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            password2 = request.POST.get('password2', '')
            if password == password2:
                user = UserInfo.objects.get(username=email)
                user.password = make_password(password)
                user.save()
            return render(request, 'login.html', {})
        else:
            return render(request, 'password_reset.html', {})