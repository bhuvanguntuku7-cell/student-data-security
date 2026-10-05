from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import UserProfile, StudentRecord, ActivityLog

@login_required
def dashboard(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    # Audit log entry for every dashboard access
    ActivityLog.objects.create(
        user=request.user,
        action=f"Accessed dashboard with role: {profile.role}"
    )

    context = {'profile': profile}

    if profile.role == 'student':
        # Limit dataset to the authenticated student's own record
        context['record'] = StudentRecord.objects.filter(student_user=request.user).first()
    elif profile.role in ['admin', 'faculty']:
        # Broad access for administrative and faculty roles
        context['all_records'] = StudentRecord.objects.all()
        context['activity_logs'] = ActivityLog.objects.all().order_by('-timestamp')[:10]

    return render(request, 'dashboard.html', context)