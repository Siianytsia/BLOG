from .base import * #noqa
from .base import env

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default = "lE9uNCFehGNu0pXz0D3Jf-40WCv7R4IS9G1Ac1VWmLWRFP61uVI",
)

DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8000"]