from webhook.api import WebhookResource
from django.contrib import admin
from django.urls import path, include

webhook_resource = WebhookResource()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(webhook_resource.urls))
]
