from pathlib import Path
import dj_database_url
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/


SECRET_KEY = os.environ.get("SECRET_KEY", "92bbc6bce4118ae1f2e0e88842c95456")


# SECURITY WARNING: don't run with debug turned on in production!
# settings.py
DEBUG = os.environ.get("DEBUG", "False") == "True"

# settings.py mein purane ALLOWED_HOSTS ko hata kar ye likhein:
ALLOWED_HOSTS = ['interior-project01.onrender.com', 'localhost', '127.0.0.1']

CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    'http://localhost:8080',
    'http://127.0.0.1:8080',
]
# For quick local testing you can also set CORS_ALLOW_ALL_ORIGINS = True (disable for production)
# Application definition

INSTALLED_APPS = [
    'cloudinary_storage', # 👈 Is line ko sabse upar le aayein
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', # Isse upar hona chahiye cloudinary_storage
    'project',
    'rest_framework', 
    'corsheaders',
    'cloudinary',
]
# settings.py

# settings.py

# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
#     'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
#     'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
# }

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dguujmj75',
    'API_KEY': '441238871653336',
    'API_SECRET': 'IdV3dJ8PFjvWzR7vqrWJajtJVog',
}
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
     
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.AllowAny", # 👈 Ise change karein
    ),
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'interior_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True, # 👈 Ye True hona zaroori hai
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug', # 👈 Ye line add karein
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'interior_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases
# settings.py mein Database section ko isse replace karein:


DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'), # Render ka URL yahan se uthayega
        conn_max_age=600,
        ssl_require=True
    )
}

# Agar DATABASE_URL nahi milti (local par), toh SQLite use karega
if not DATABASES['default']:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

# settings.py ke aakhiri mein ye pura block paste kar dein

# Cloudinary Credentials
# settings.py के अंत में इसे पेस्ट करें

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dguujmj75',
    'API_KEY': '441238871653336',
    'API_SECRET': 'IdV3dJ8PFjvWzR7vqrWJajtJVog',
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Static files (Whitenoise use kar rahe hain)
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = BASE_DIR / "staticfiles"

# Media settings (Local testing ke liye)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')