from django.shortcuts import render, redirect
from .forms import SignupForm
from gbtaluka.models import UserDetail

def index_view(request):
    return render(request, 'index.html', {})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid:
            user = form.save()
            user_detail = UserDetail(user=user)
            user_detail.save()
            return redirect('gbtaluka:profile')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})
