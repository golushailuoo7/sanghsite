from django.shortcuts import render, redirect
from .forms import SignupForm
from gbtaluka.models import UserDetail, NoticeBoard
from django.contrib.auth.models import User
from django.utils import timezone

def index_view(request):
    if request.user.is_authenticated():
        return redirect('gbtaluka:profile')
    notice_bar = NoticeBoard.objects.filter(to_date__lte=timezone.now())
    return render(request, 'index.html', {'notice_bar': notice_bar})

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
                return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})
