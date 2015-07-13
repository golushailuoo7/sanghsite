from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import UpdateProfile


@login_required
def profile_view(request):
    return render(request, 'gbtaluka/profile.html', {})


@login_required
def update_profile_view(request):
    if request.method == 'POST':
        form = UpdateProfile(request.POST, request.FILES)
        if form.is_valid():
            user_entry = form.save()
            return redirect('gbtaluka:profile')
    else:
        form = UpdateProfile()
    return render(request, 'gbtaluka/update_profile.html', {'form': form})

