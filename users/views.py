from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from .models import CustomUser
from django.contrib.auth import login as slogin, authenticate, logout as slogout
import json
from django.core.mail import send_mail
from monitor_app.settings import EMAIL_FROM
from django.http import HttpResponse


# Create your views here.
def signup(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        message = "please complete forms！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']

        if password1 != password2:
            message = "different password input！"
            return render(request, 'register.html', locals())
        else:
            same_name_user = CustomUser.objects.filter(username=username)
            if same_name_user:
                message = 'user already exist!'
                return render(request, 'register.html', locals())
            same_email_user = CustomUser.objects.filter(email=email)
            if same_email_user:
                message = 'email already exist!'
                return render(request, 'register.html', locals())

            new_user = CustomUser.objects.create_user(username=username, password=password1, email=email,
                                                      sub_email=email)
            new_user.save()
            return redirect('/users/login/')  # 自动跳转到登录页面
    else:
        register_form = RegisterForm()
        return render(request, 'register.html', locals())


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        message = "please check forms！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                slogin(request, user)
                print("OK................")
                return redirect('/index')
            else:
                message = "loging error"
                return render(request, 'login.html', locals())
        return render(request, 'login.html', locals())
    else:
        login_form = LoginForm()
        return render(request, 'login.html', locals())


def logout(request):
    slogout(request)
    return redirect('login/')


def addURL(request):
    if request.method == 'POST':
        user = request.user
        jsonDec = json.decoder.JSONDecoder()
        if user.myList:
            urls = jsonDec.decode(user.myList)
        else:
            urls = []
        url = request.POST.get("new-url")
        urls.append(url)
        user.myList = json.dumps(urls)
        user.save()
        return redirect('/index')
    else:
        return redirect('/index')


def sub_email(request):
    if request.method == 'POST':
        user = request.user
        user.sub_email = request.POST.get("sub_email")
        user.save()
        return redirect('/settings')
    else:
        return redirect('/settings')


def send_test(request):
    user  = request.user
    email_title = 'Monitor App Notification Test'
    email_body = 'Test Email'
    email = user.sub_email
    res = send_mail(email_title, email_body, EMAIL_FROM, [email])
    return HttpResponse(res)
