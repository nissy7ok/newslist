from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, get_user_model
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .forms import SignUpForm
from datetime import date
from django.contrib import messages

User = get_user_model()

def home(request):
    return render(request, 'newslistapp:index')

def signup(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            auth_login(request, user)
            messages.success(request, '登録内容を保存しました')
            return redirect('newslistapp:index')
    else:
        signup_form = SignUpForm()
    return render(request, 'signup.html', {'signup_form': signup_form})
    messages.error(request, '登録内容の保存に失敗しました')