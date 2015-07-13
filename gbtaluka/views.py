from django.shortcuts import render, redirect
from django.utils import timezone

from django.contrib.auth.decorators import login_required

from .forms import UpdateProfile
from .models import Responsibility, NoticeBoard


@login_required
def profile_view(request):
    user_detail = request.user.userdetail
    notice_bar = NoticeBoard.objects.filter(to_date__lte=timezone.now())
    return render(request, 'gbtaluka/profile.html', {'detail': user_detail, 'notice_bar': notice_bar})


@login_required
def update_profile_view(request):
    if request.method == 'POST':
        form = UpdateProfile(request.POST,
                request.FILES,
                instance=request.user.userdetail)
        if form.is_valid():
            user_entry = form.save(commit=False)
            user_entry.responsibility = Responsibility.objects.get(
                level=8)
            user_entry.save()
            return redirect('gbtaluka:profile')
    else:
        form = UpdateProfile(instance=request.user.userdetail)
    return render(request, 'gbtaluka/update_profile.html', {'form': form})

