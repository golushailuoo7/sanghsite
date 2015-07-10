from django.contrib import admin

from .models import Shakha, Responsibility, UserDetail, FamilyDetail, EventDetail, NoticeBoard


admin.site.register(Shakha)
admin.site.register(Responsibility)
admin.site.register(UserDetail)
admin.site.register(FamilyDetail)
admin.site.register(EventDetail)
admin.site.register(NoticeBoard)
