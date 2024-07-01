from django.contrib import admin
from .models import Member, Category, Announcement, AnnouncementCategory, Respond, Subscriber

# Register your models here.
admin.site.register(Member)
admin.site.register(Category)
admin.site.register(Announcement)
admin.site.register(AnnouncementCategory)
admin.site.register(Respond)
admin.site.register(Subscriber)
