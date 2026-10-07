from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
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
        context['record'] = StudentRecord.objects.filter(student_user=request.user).first()
    elif profile.role in ['admin', 'faculty']:
        # Broad access for administrative and faculty roles
        context['all_records'] = StudentRecord.objects.all()
        context['activity_logs'] = ActivityLog.objects.all().order_by('-timestamp')
    return render(request, 'dashboard.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically assign the student role to new sign-ups
            UserProfile.objects.create(user=user, role='student')
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    """Custom view to handle logout via both GET and POST without HTTP 405 errors."""
    logout(request)
    return redirect('login')