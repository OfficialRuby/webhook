from django.db import models


class Webhook(models.Model):
    event = models.CharField(max_length=50)
    data = models.JSONField()

    def __str__(self):
        return self.event
