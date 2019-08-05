from django.shortcuts import render

# Create your views here.
import logging
#
from django.core import serializers
# import json
import numpy
from django.db.models import F
import random
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse
from django.shortcuts import redirect
# from django.shortcuts import render_to_response
from django.shortcuts import render
from django.db.models import Q
from .models import User
from . import models
import numpy as np
from django.core.paginator import Paginator


def index(request):
    print("ok entered!")
    return render(request, "index/index.html")


def back_index(request):
    return render(request, "index/main.html")


def signIn(request):
    print("You enter the method of login")
    return render(request, "sign_in_up/signIn.html")


def signIn_process(request):
    # user_info = request.POST['user_info']
    # user_password = request.POST['user_password']
    user_info = request.POST.get('user_info')
    user_password = request.POST.get('user_password')
    user = models.User.objects.filter(
        (Q(user_name=user_info) | Q(user_email=user_info)) & Q(
            user_password=user_password)).first()
    if user:
        return render(request, "index/main.html", {"user": user})

    return render(request, "sign_in_up/signIn.html", {"login_failure": "failure"})


def signUp(request):
    return render(request, "sign_in_up/signUp.html")


def signUp_process(request):
    user_name = request.POST.get('user_name')
    user_email = request.POST.get('user_email')
    user_password = request.POST.get('user_password')
    print(user_email+"--"+user_name+"--"+user_password);
    user = User(
        user_name=user_name,
        user_email=user_email,
        user_password=user_password,
    )
    user.save()
    # return render(request, "sign_in_up/signUp.html", {"register_success": "success"})
    return render(request, "index/index.html")


def textChat(request):
    return render(request, "chat_bot/textChat.html")


def textChat_component(request):
    return render(request, "chat_bot/textChat_component.html")


def voiceChat(request):
    return render(request, "chat_bot/voiceChat.html")


def voiceChat_component(request):
    return render(request, "chat_bot/voiceChat_component.html")
