from django.contrib import admin

from .models import Shakha, Responsibility, BasicDetail, FamilyDetail, EventDetail, NoticeBoard


admin.site.register(Shakha)
admin.site.register(Responsibility)
admin.site.register(BasicDetail)
admin.site.register(FamilyDetail)
admin.site.register(EventDetail)
admin.site.register(NoticeBoard)
