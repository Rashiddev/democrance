# SECURITY WARNING: keep the secret key used in production secret!
import os

from democrance.settings import BASE_DIR

SECRET_KEY = 'tuiwhg#b9%qx)(xt%15=5!2gt@xri=wiwel(e7_8^h5f4rc(tf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
