from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import UpdateProfile, UserSearch
from .models import Responsibility, NoticeBoard


@login_required
def profile_view(request):
    user_detail = request.user.userdetail
    notice_bar = NoticeBoard.objects.filter(to_date__lte=timezone.now())
    if request.method == 'POST':
        form = UserSearch(request.POST)
        if form.is_valid():
            first = form.cleaned_data['first_name']
            last = form.cleaned_data['last_name']
            if first == "" and last == "":
                first = " "
                last = " "
            users = User.objects.filter(first_name__icontains=first,
                    last_name__icontains=last)
            return render(request,
                'gbtaluka/profile.html',
                {'detail': user_detail,
                    'notice_bar': notice_bar,
                    'form': form,
                    'users': users})
    else:
        form = UserSearch()
    return render(request,
        'gbtaluka/profile.html',
        {'detail': user_detail, 'notice_bar': notice_bar, 'form': form})


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



@login_required
def user_view(request, username):
    this_user_detail = get_object_or_404(User, username=username).userdetail
    user_detail = request.user.userdetail
    notice_bar = NoticeBoard.objects.filter(to_date__lte=timezone.now())
    return render(request,
        'gbtaluka/user.html',
        {'detail': user_detail, 'notice_bar': notice_bar, 'this_user_detail': this_user_detail})

