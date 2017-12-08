from base import *
import dj_database_url

DEBUG = False
 
# Load the ClearDB connection details from the environment variable
DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}
 
# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_2jElTRtzMvtW5zNLI7gI0vSz')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_hfA92LDhjAkrzBbDiifmA3IN')

# PayPal Settings
SITE_URL = 'http://127.0.0.1:8000'
PAYPAL_NOTIFY_URL = 'http://127.0.0.1/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'kaiforward123-facilitator@gmail.com'
 
SITE_URL = 'https://the-galactic-index.herokuapp.com'
ALLOWED_HOSTS.append('the-galactic-index.herokuapp.com')
 
# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}

