from base import *
 
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
 
# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_2jElTRtzMvtW5zNLI7gI0vSz')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_hfA92LDhjAkrzBbDiifmA3IN')

# PayPal Settings
SITE_URL = 'http://127.0.0.1:8000'
PAYPAL_NOTIFY_URL = 'http://127.0.0.1/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'kaiforward123-facilitator@gmail.com'