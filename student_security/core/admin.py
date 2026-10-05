from django.contrib import admin
from .models import UserProfile, StudentRecord, ActivityLog

admin.site.register(UserProfile)
admin.site.register(StudentRecord)
admin.site.register(ActivityLog)