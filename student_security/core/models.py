from django.db import models
from django.contrib.auth.models import User

# Role-Based Access Control (RBAC) Profile
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Administrator'),
        ('faculty', 'Faculty'),
        ('student', 'Student'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    department = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

# Student Record Management
class StudentRecord(models.Model):
    student_user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20, unique=True)
    academic_year = models.CharField(max_length=20)
    attendance = models.FloatField(default=0.0)
    exam_results = models.TextField(blank=True, help_text="Marks/Grades")
    certificates_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.roll_number} - {self.student_user.get_full_name()}"

# Activity Logging
class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.timestamp} - {self.user} - {self.action}"