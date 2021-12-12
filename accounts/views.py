from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from accounts.models import  User, Referral
from .forms import  MyUserCreationForm
from knonapp import *






def login_view(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Username OR Password does not exit')

    context = {'page': page}
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('newsletter')


def register_view(request):
    profile_id = request.session.get('ref_profile')
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            if profile_id is not None:
                recommended_by_ref = Referral.objects.get(id=profile_id)
                instance = form.save()
                registered_user = User.objects.get(id=instance.id)
                registered_profile = Referral.objects.get(user=registered_user)
                registered_profile.recommended_by = recommended_by_ref.user
                registered_profile.save()
                return redirect('login')
            else:
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                login(request, user)
                return redirect('dashboard')
        else:
           messages.error(request, 'An error occurred during registration')

    return render(request, 'register.html', {'form': form})



def referrals(request, *args, **kwargs):
    code = str(kwargs.get('ref_code'))
    try:
        referral = Referral.objects.get(code=code)
        request.session['ref_profile'] = referral.id
    except:
        pass
    return render(request,'dashboard.html')




