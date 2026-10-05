from pathlib import Path

# 1. Base directory definition
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Security settings
SECRET_KEY = 'django-insecure-your-secret-key-goes-here'
DEBUG = True
ALLOWED_HOSTS = ['student-data-security.onrender.com','localhost','127.0.0.1']

# 3. Installed applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # Your application
]

# 4. Middleware configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'student_security.urls'

# 5. Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'student_security.wsgi.application'

# 6. Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 7. Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 8. Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 9. Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# 10. Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 11. Security & Authentication redirects
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'login'

STATIC_ROOT=BASE_DIR/'staticfiles'


import os
from django.contrib.auth import get_user_model

def create_or_reset_superuser():
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

try:
    create_or_reset_superuser()
except Exception:
    pass