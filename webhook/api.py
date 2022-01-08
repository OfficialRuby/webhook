from webhook.models import Webhook
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.models import ApiKey
from django.contrib.auth.models import User

# paystack = User.objects.get(User, username=paystack)
# http: // localhost: 8000/api/expense /?username=paystack&api_key=1a23


# ApiKey.objects.create(key='1a23', user=paystack)

class WebhookResource(ModelResource):
    class Meta:
        queryset = Webhook.objects.all()
        resource_name = 'webhook'
        fields = ['event',  'data', ]
        authorization = Authorization()
        # authentication = ApiKeyAuthentication()
