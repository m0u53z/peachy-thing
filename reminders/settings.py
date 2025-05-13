INSTALLED_APPS = [
    # ... default django apps
    'rest_framework',
    'reminders',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# (Adjust TIME_ZONE, etc., as needed)

