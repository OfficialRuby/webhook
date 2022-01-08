from webhook.models import Webhook
from django.db.models.signals import post_save
import json


def save_profile(sender, instance, **kwargs):
    data = instance.data
    ref = data['reference']
    print(ref)


post_save.connect(save_profile, sender=Webhook)
