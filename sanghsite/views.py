from django.shortcuts import render, redirect
from .forms import SignupForm
from gbtaluka.models import UserDetail
from django.contrib.auth.models import User

def index_view(request):
    return render(request, 'index.html', {})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['confirm_password']:
                user = User.objects.create_user(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email'])
                user.set_password(form.cleaned_data['password'])
                user_detail = UserDetail(user=user)
                user_detail.save()
                return redirect('gbtaluka:profile')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})
