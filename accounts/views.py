from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, get_user_model
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .forms import SignUpForm
from datetime import date

User = get_user_model()

def home(request):
    return render(request, 'newslistapp:index')

def signup(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            username = signup_form.cleaned_data.get('username')
            email = signup_form.cleaned_data.get('email')
            password = signup_form.cleaned_data.get('password')

            user = User.objects.create_user(username, email, password)
            user.save()

            user = authenticate(request, username=username, password=password)
            auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.add_message(request, messages.SUCCESS, 'ユーザー登録が完了しました！')
            return redirect('newslistapp:index')
    else:
        signup_form = SignUpForm()

    # login_form = LoginForm()
    context = {
        'signup_form': signup_form,
    }
    return render(request, 'signup.html', context)
