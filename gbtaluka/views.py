from PIL import Image

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

from .forms import UpdateProfile, UserSearch, CreateShakha, EditResponsibility, AddNotification
from .models import Responsibility, NoticeBoard, Shakha, UserDetail


def only_taluka_level_user(user):
    return user.userdetail.responsibility.level <= 4


@login_required
def profile_view(request):
    user_detail = request.user.userdetail
    notice_bar = NoticeBoard.objects.filter(to_date__gte=timezone.now())
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
            user_entry = form.save()
            if request.FILES:
                im = Image.open(user_entry.picture.path)
                im.thumbnail((512, 512))
                im.save(user_entry.picture.path, "JPEG")
            return redirect('gbtaluka:profile')
    else:
        form = UpdateProfile(instance=request.user.userdetail)
    return render(request, 'gbtaluka/update_profile.html', {'form': form})


@login_required
def user_view(request, username):
    this_user_detail = get_object_or_404(User, username=username).userdetail
    user_detail = request.user.userdetail
    notice_bar = NoticeBoard.objects.filter(to_date__gte=timezone.now())
    return render(request,
        'gbtaluka/user.html',
        {'detail': user_detail, 'notice_bar': notice_bar, 'this_user_detail': this_user_detail})


@user_passes_test(only_taluka_level_user)
@login_required
def add_shakha_view(request):
    if request.method == 'POST':
        form = CreateShakha(request.POST)
        if form.is_valid():
            form.save()
        return redirect('gbtaluka:profile')
    else:
        form = CreateShakha()
    return render(request, 'gbtaluka/add_shakha.html', {'form': form})


def shakhas_view(request):
    shakhas = Shakha.objects.all()
    return render(request, 'gbtaluka/shakhas.html', {'shakhas': shakhas})


@login_required
def shakha_view(request, shakha_id):
    shakha_users = UserDetail.objects.filter(shakha__pk=shakha_id)
    shakha = Shakha.objects.get(pk=shakha_id)
    return render(request, 'gbtaluka/shakha.html', {'shakha_users': shakha_users, 'shakha': shakha})



@user_passes_test(only_taluka_level_user)
@login_required
def edit_shakha_view(request, shakha_id):
    shakha = Shakha.objects.get(pk=shakha_id)
    if request.method == 'POST':
        form = CreateShakha(request.POST, instance=shakha)
        if form.is_valid():
            form.save()
        return redirect('gbtaluka:shakhas')
    else:
        form = CreateShakha(instance=shakha)
    return render(request, 'gbtaluka/edit_shakha.html', {'form': form, 'shakha':shakha})


def contacts_view(request):
    contact_users = UserDetail.objects.filter(responsibility__level__lte=6).order_by('responsibility__level')
    return render(request, 'gbtaluka/contacts.html', {'contact_users': contact_users})


@user_passes_test(only_taluka_level_user)
@login_required
def edit_responsibility_view(request, user_id):
    user_detail = User.objects.get(pk=user_id).userdetail
    if request.method == 'POST':
        form = EditResponsibility(request.POST, instance=user_detail)
        if form.is_valid():
            form.save()
        return redirect('gbtaluka:profile')
    else:
        form = EditResponsibility(instance=user_detail)
    return render(request, 'gbtaluka/edit_responsibility.html', {'form': form, 'user_detail': user_detail})


@user_passes_test(only_taluka_level_user)
@login_required
def add_notification_view(request):
    if request.method == 'POST':
        form = AddNotification(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gbtaluka:profile')
    else:
        form = AddNotification()
    return render(request, 'gbtaluka/add_notification.html', {'form': form})
