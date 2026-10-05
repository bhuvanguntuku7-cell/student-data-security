import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_security.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
username = 'admin'
password = 'AdminPassword123!'

user, created = User.objects.get_or_create(
    username=username,
    defaults={'email': 'admin@example.com', 'is_staff': True, 'is_superuser': True}
)

user.is_staff = True
user.is_superuser = True
user.set_password(password)
user.save()

print("Superuser admin created/reset successfully!")