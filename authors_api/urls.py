from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Authors Heaven API", 
        default_version="v1", 
        description="API endpoints for Authors Heaven API Course",
        contact=openapi.Contact(email="pilipsia@gmail.com"),
        license=openapi.License(name="MIT license") 
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0)),
    path(settings.ADMIN_URL, admin.site.urls),
]

admin.site.site_header = "Authors Heaven API Admin"

admin.site.site_title = "Authors Heaven API Admin Portal"

admin.site.index_title = "Welcome to Authors Heaven API Portal"
