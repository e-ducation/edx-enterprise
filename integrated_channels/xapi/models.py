"""
Models for X-API.
"""
import base64

from django.db import models

from model_utils.models import TimeStampedModel


class XAPILRSConfiguration(TimeStampedModel):
    """
    X-API LRS configurations.
    """
    version = models.CharField(max_length=16, default='1.0.1')
    endpoint = models.URLField(help_text='URL of the LRS.')
    key = models.CharField(max_length=100, unique=True)
    secret = models.CharField(max_length=255, unique=True)

    @property
    def authorization_header(self):
        return 'Basic {}'.format(
            base64.b64encode('{key}:{secret}'.format(key=self.key, secret=self.secret).encode()).decode()
        )
