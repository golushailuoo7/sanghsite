import datetime

from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.models import User

from .models import UserDetail

cur_year = datetime.date.today().year


class UpdateProfile(forms.ModelForm):
    class Meta:
        model = UserDetail
        exclude = ['user', 'responsibility', 'publish',]

        widgets = {
            'date_of_birth': SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"), years=range(1900, cur_year+1)),
            'joining_date': SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"), years=range(1900, cur_year+1)),
        }


class UserSearch(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name',]
