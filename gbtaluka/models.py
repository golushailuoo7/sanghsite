from django.db import models
from django.contrib.auth.models import User
import datetime


O_MINUS = 'O-'
O_PLUS = 'O+'
A_MINUS = 'A-'
A_PLUS = 'A+'
B_MINUS = 'B-'
B_PLUS = 'B+'
AB_MINUS = 'AB-'
AB_PLUS = 'AB+'

BLOOD_TYPES = (
    (O_MINUS, 'O Minus'),
    (O_PLUS, 'O Plus'),
    (A_MINUS, 'A Minus'),
    (A_PLUS, 'A Plus'),
    (B_MINUS, 'B Minus'),
    (B_PLUS, 'B Plus'),
    (AB_MINUS, 'AB Minus'),
    (AB_PLUS, 'AB Plus'),
)


def content_file_name(instance, filename):
        return '/'.join(['profile_pic',
            instance.user.username,
            '_'.join([
                str(datetime.date.today()),
                str(datetime.datetime.time(datetime.datetime.now()))
                ])
            ])


class Shakha(models.Model):
    MORNING = 'MG'
    EVENING = 'EV'
    NIGHT = 'NT'
    WEEKLY_MORNING = 'WM'
    WEEKLY_EVENING = 'WE'
    WEEKLY_NIGHT = 'WN'

    TYPES = (
        (MORNING, 'Morning'),
        (EVENING, 'Evening'),
        (NIGHT, 'Night'),
        (WEEKLY_MORNING, 'Weekly morning'),
        (WEEKLY_EVENING, 'Weekly evening'),
        (WEEKLY_NIGHT, 'Weekly night'),
    )

    shakha_name = models.CharField(max_length=200)
    shakha_time = models.TimeField('shakha time')
    shakha_type = models.CharField(max_length=2, choices=TYPES)
    shakha_venue = models.CharField(max_length=400)

    def __str__(self):
        return "{} {}".format(self.shakha_name, self.shakha_type)


class Responsibility(models.Model):
    responsibility = models.CharField(max_length=200)
    level = models.IntegerField()

    def __str__(self):
        return self.responsibility


class UserDetail(models.Model):

    JOIN_RSS = 'JOINRSS'
    FRIENDS = 'FRIENDS'
    FAMILY = 'FAMILY'
    SCHOOL = 'SCHOOL'
    OTHER = 'OTHER'

    JOIN_SOURCE = (
        (JOIN_RSS, 'Through Join Rss'),
        (FRIENDS, 'Through Friends'),
        (FAMILY, 'Through Family'),
        (SCHOOL, 'Through School/Collage'),
        (OTHER, 'Any other source'),
    )

    user = models.OneToOneField(User)
    shakha = models.ForeignKey(Shakha, null=True, blank=True)
    responsibility = models.ForeignKey(Responsibility, null=True, blank=True)
    gatnayak = models.ForeignKey("UserDetail", related_name='gatnayak_fk', null=True, blank=True)
    picture = models.ImageField(upload_to=content_file_name, null=True, blank=True)
    date_of_birth = models.DateField('date of birth', null=True, blank=True)
    contact_number = models.CharField(max_length=10, null=True, blank=True)
    blood_group = models.CharField(max_length=3, choices=BLOOD_TYPES, null=True, blank=True)
    address = models.CharField(max_length=400, null=True, blank=True)
    education = models.CharField(max_length=200, null=True, blank=True)
    occupation = models.CharField(max_length=200, null=True, blank=True)
    hobbies = models.CharField(max_length=300, null=True, blank=True)
    joining_date = models.DateField('date joined', null=True, blank=True)
    source_of_joining = models.CharField(max_length=10, choices=JOIN_SOURCE, null=True, blank=True)
    prathmik_completed = models.BooleanField(default=False)
    prathm_varsh_completed = models.BooleanField(default=False)
    dwitiya_varsh_completed = models.BooleanField(default=False)
    tratiya_varsh_completed = models.BooleanField(default=False)
    shirt = models.BooleanField(default=False)
    pants = models.BooleanField(default=False)
    socks = models.BooleanField(default=False)
    shoes = models.BooleanField(default=False)
    cap = models.BooleanField(default=False)
    belt = models.BooleanField(default=False)
    bamboo_staff = models.BooleanField(default=False)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return "{}@{}".format(self.user.first_name, self.user.username)


class FamilyDetail(models.Model):
    basic_detail = models.ForeignKey(UserDetail)
    relative_name = models.CharField(max_length=200)
    relation = models.CharField(max_length=200)
    education = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200)
    blood_group = models.CharField(max_length=3, choices=BLOOD_TYPES)
    date_of_birth = models.DateField('date of birt')

    def __str__(self):
        return "{}: {}@{}".format(
            self.relative_name,
            self.basic_detail.user.first_name,
            self.basic_detail.user.username)


class EventDetail(models.Model):
    responsibility = models.ForeignKey(Responsibility)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    start_time = models.DateTimeField('start time')
    end_time = models.DateTimeField('end time')
    venue = models.CharField(max_length=400)

    def __str__(self):
        return "{}@{}".format(self.title, self.responsibility.responsibility)


class NoticeBoard(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    from_date = models.DateTimeField('start time')
    to_date = models.DateTimeField('end time')

    def __str__(self):
        return self.title

