from .base import * #noqa
from .base import env

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default = "lE9uNCFehGNu0pXz0D3Jf-40WCv7R4IS9G1Ac1VWmLWRFP61uVI",
)

DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8000"]

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "support@apiimperfect.site"
DOMAIN = env("DOMAIN")
SITE_NAME = "Authors Haven"