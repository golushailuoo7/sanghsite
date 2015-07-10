from django.shortcuts import render


def profile_view(request):
    return render(request, 'gbtaluka/profile.html', {'cur_user': request.user})
